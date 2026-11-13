"""
Moteur de RAG (Retrieval-Augmented Generation) pour Nantes Métropole.
Indexation en SQLite FTS5 (Full-Text Search avec ranking BM25) + scoring sémantique.
Permet d'extraire les passages les plus pertinents pour enrichir le prompt de l'IA.
"""

import sqlite3
import re
import unicodedata
from typing import List, Dict, Any
from app.knowledge_data import get_all_chunks

def normalize_text(text: str) -> str:
    """Supprime les accents et met en minuscules pour faciliter la recherche."""
    if not text:
        return ""
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = "".join(c for c in text if unicodedata.category(c) != 'Mn')
    return text

class NantesRAGEngine:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.chunks_by_id: Dict[str, Dict[str, Any]] = {}
        self._init_database()

    def _init_database(self):
        """Initialise la table FTS5 et indexe les connaissances."""
        cursor = self.conn.cursor()
        
        # Création de la table virtuelle FTS5 avec BM25
        cursor.execute("DROP TABLE IF EXISTS fts_knowledge")
        cursor.execute("""
            CREATE VIRTUAL TABLE fts_knowledge USING fts5(
                chunk_id UNINDEXED,
                category UNINDEXED,
                title,
                keywords,
                content,
                tokenize = 'unicode61 remove_diacritics 2'
            )
        """)

        chunks = get_all_chunks()
        for chunk in chunks:
            self.chunks_by_id[chunk["id"]] = chunk
            keywords_str = " ".join(chunk.get("keywords", []))
            cursor.execute(
                "INSERT INTO fts_knowledge(chunk_id, category, title, keywords, content) VALUES (?, ?, ?, ?, ?)",
                (
                    chunk["id"],
                    chunk["category"],
                    chunk["title"],
                    keywords_str,
                    chunk["content"]
                )
            )
        self.conn.commit()

    def search(self, query: str, top_k: int = 4) -> List[Dict[str, Any]]:
        """
        Recherche les chunks les plus pertinents pour une question donnée.
        Combine recherche FTS5 et boost par mots-clés.
        """
        if not query or not query.strip():
            # Si pas de query, retourne 3 incontournables
            return [self.chunks_by_id[k] for k in ["transports_gratuite_weekend", "patrimoine_machines_ile", "hotel_recommandations_quartiers"]]

        clean_q = re.sub(r'[^\w\s]', ' ', query)
        words = [w for w in clean_q.split() if len(w) > 2]
        
        results = []
        seen_ids = set()

        if words:
            # Construction d'une requête FTS5 robuste avec OR et préfixes
            fts_query = " OR ".join([f'"{w}"*' for w in words])
            cursor = self.conn.cursor()
            
            try:
                # FTS5 bm25 ranking (les scores les plus négatifs sont les meilleurs)
                cursor.execute("""
                    SELECT chunk_id, bm25(fts_knowledge, 10.0, 5.0, 1.0) AS score
                    FROM fts_knowledge
                    WHERE fts_knowledge MATCH ?
                    ORDER BY score ASC
                    LIMIT ?
                """, (fts_query, top_k * 2))
                
                rows = cursor.fetchall()
                for chunk_id, score in rows:
                    if chunk_id in self.chunks_by_id and chunk_id not in seen_ids:
                        seen_ids.add(chunk_id)
                        chunk = dict(self.chunks_by_id[chunk_id])
                        chunk["relevance_score"] = round(float(score), 3)
                        results.append(chunk)
            except sqlite3.OperationalError:
                # Fallback si syntaxe complexe
                pass

        # Recherche de secours par correspondance de mots clés normalisés
        norm_query = normalize_text(query)
        for chunk_id, chunk in self.chunks_by_id.items():
            if chunk_id in seen_ids:
                continue
            
            score = 0
            # Vérification du titre
            if normalize_text(chunk["title"]) in norm_query or any(w in normalize_text(chunk["title"]) for w in words):
                score += 3
            # Vérification des keywords
            for kw in chunk.get("keywords", []):
                if kw in norm_query:
                    score += 2
                elif any(w == normalize_text(kw) for w in words):
                    score += 1
            
            if score > 0:
                item = dict(chunk)
                item["relevance_score"] = -score  # compatible avec bm25 asc
                results.append(item)
                seen_ids.add(chunk_id)

        # Trie par score ascendant (meilleurs scores en premier)
        results.sort(key=lambda x: x.get("relevance_score", 0))
        selected = results[:top_k]

        # Si aucun résultat trouvé, fallback vers les connaissances générales
        if not selected:
            selected = [
                self.chunks_by_id["transports_gratuite_weekend"],
                self.chunks_by_id["patrimoine_chateau_ducs"],
                self.chunks_by_id["hotel_recommandations_quartiers"]
            ]

        return selected

    def build_rag_context(self, retrieved_chunks: List[Dict[str, Any]]) -> str:
        """
        Assemble le contexte documentaire extrait pour l'injecter au prompt système.
        """
        context_parts = []
        for i, chunk in enumerate(retrieved_chunks, 1):
            category = chunk.get('category', '').upper()
            title = chunk.get('title', '')
            content = chunk.get('content', '')
            context_parts.append(f"[SOURCE {i}] ({category}) : {title}\n{content}")
        
        return "\n\n".join(context_parts)

# Instance singleton
rag_engine = NantesRAGEngine()

