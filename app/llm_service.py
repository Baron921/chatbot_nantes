"""
Service de génération par IA (LLM) avec RAG pour Nantes Métropole.
Supporte Google Gemini (recommandé) et OpenAI (GPT-4o / GPT-4o-mini).
Inclut un mode démonstration intelligent si la clé n'est pas encore configurée.
"""

import os
import requests
from typing import List, Dict, Any, Optional

SYSTEM_PROMPT_TEMPLATE = """Tu es « Naomì », l'assistant virtuel intelligent et chaleureux de Nantes Métropole.
Ton rôle est d'informer avec précision les habitants, touristes et visiteurs sur :
- Les TRANSPORTS en commun (Réseau Naolib : tramway, bus, busway, navibus, gratuité chaque week-end, vélos Bicloo, accès aéroport).
- Les LIEUX HISTORIQUES et culturels (Château des ducs de Bretagne, Machines de l'Île, Passage Pommeraye, Jardin des Plantes, Ligne Verte du Voyage à Nantes, Trentemoult, etc.).
- Les HÔTELS et hébergements (conseils par quartier, budgets, adresses de charme ou insolites comme le Sozo Hôtel).
- La GASTRONOMIE nantaise (gâteau nantais, Muscadet, Curé nantais, berlingots, Marché de Talensac, brasserie La Cigale).
- Les bons plans et itinéraires de visite.

RÈGLES IMPORTANTES :
1. Fais référence en priorité aux informations du CONTEXTE DOCUMENTAIRE fourni ci-dessous.
2. Si une information est présente dans le contexte (comme la gratuité des transports le week-end du samedi 0h au dimanche 23h59), mentionne-la clairement avec enthousiasme.
3. Sois précis, poli, accueillant et structure ta réponse avec du Markdown (titres, listes à puces, gras, emojis appropriés).
4. Si la question est générale ou hors sujet, réponds brièvement et ramène poliment l'échange vers Nantes Métropole et ses services.

=== CONTEXTE DOCUMENTAIRE EXTRAIT DE LA BASE NANTES MÉTROPOLE ===
{rag_context}
================================================================
"""

class LLMService:
    def __init__(self):
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def _get_api_key(self, provider: str, user_key: Optional[str] = None) -> Optional[str]:
        """Récupère la clé API soit depuis l'argument utilisateur, soit depuis les variables d'environnement."""
        if user_key and user_key.strip():
            return user_key.strip()
        
        if provider == "openai":
            return os.getenv("OPENAI_API_KEY")
        else:
            # Gemini ou Google
            return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    def call_gemini(self, message: str, rag_context: str, history: List[Dict[str, str]], api_key: str) -> str:
        """Appel direct à l'API REST Google Gemini."""
        system_instruction = SYSTEM_PROMPT_TEMPLATE.format(rag_context=rag_context)
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.gemini_model}:generateContent?key={api_key}"
        
        contents = []
        # Historique
        for turn in history[-6:]: # 3 derniers échanges max
            role = "user" if turn.get("role") == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": turn.get("content", "")}]
            })
            
        # Message actuel
        contents.append({
            "role": "user",
            "parts": [{"text": message}]
        })

        payload = {
            "system_instruction": {
                "parts": [{"text": system_instruction}]
            },
            "contents": contents,
            "generationConfig": {
                "temperature": 0.5,
                "maxOutputTokens": 1024,
            }
        }

        response = requests.post(url, json=payload, timeout=25)
        
        if response.status_code != 200:
            error_data = response.json() if response.content else {}
            err_msg = error_data.get("error", {}).get("message", response.text)
            raise RuntimeError(f"Erreur API Gemini ({response.status_code}) : {err_msg}")
        
        data = response.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return "Désolé, aucune réponse n'a été générée par le modèle."
        
        parts = candidates[0].get("content", {}).get("parts", [])
        text_response = "".join(part.get("text", "") for part in parts)
        return text_response

    def call_openai(self, message: str, rag_context: str, history: List[Dict[str, str]], api_key: str) -> str:
        """Appel à l'API OpenAI via requests / endpoint chat completions."""
        system_instruction = SYSTEM_PROMPT_TEMPLATE.format(rag_context=rag_context)
        
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        messages = [{"role": "system", "content": system_instruction}]
        for turn in history[-6:]:
            role = "user" if turn.get("role") == "user" else "assistant"
            messages.append({"role": role, "content": turn.get("content", "")})
        messages.append({"role": "user", "content": message})

        payload = {
            "model": self.openai_model,
            "messages": messages,
            "temperature": 0.5,
            "max_tokens": 1024
        }

        response = requests.post(url, headers=headers, json=payload, timeout=25)
        if response.status_code != 200:
            error_data = response.json() if response.content else {}
            err_msg = error_data.get("error", {}).get("message", response.text)
            raise RuntimeError(f"Erreur API OpenAI ({response.status_code}) : {err_msg}")
        
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def generate_response(
        self,
        message: str,
        rag_context: str,
        sources: List[Dict[str, Any]],
        history: Optional[List[Dict[str, str]]] = None,
        provider: str = "gemini",
        user_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Coordonne la génération de la réponse avec RAG.
        Si la clé API n'est pas fournie, renvoie une réponse guidée basée sur le RAG.
        """
        history = history or []
        api_key = self._get_api_key(provider, user_key)

        if not api_key:
            # Mode d'attente de configuration de clé API
            return {
                "status": "missing_api_key",
                "provider": provider,
                "text": (
                    "👋 **Bienvenue sur le Chatbot de Nantes Métropole !**\n\n"
                    "Le moteur **RAG** a bien extrait les informations locales pertinentes sur Nantes pour votre question, "
                    "mais aucune clé API (**Gemini** ou **OpenAI**) n'est encore enregistrée pour alimenter la génération IA en langage naturel.\n\n"
                    "👉 **Pour activer l'IA instantanément :**\n"
                    "1. Cliquez sur l'icône **⚙️ Paramètres** en haut à droite (ou éditez le fichier `.env`).\n"
                    "2. Renseignez votre clé API gratuite [Google Gemini API](https://aistudio.google.com/) ou OpenAI.\n\n"
                    "--- \n\n"
                    "### 📖 Extraits de connaissances trouvés pour votre question :\n"
                    + "\n\n".join([f"**📍 {s.get('title')}**\n{s.get('content')}" for s in sources[:2]])
                ),
                "is_fallback": True
            }

        try:
            if provider == "openai":
                answer = self.call_openai(message, rag_context, history, api_key)
            else:
                answer = self.call_gemini(message, rag_context, history, api_key)

            return {
                "status": "success",
                "provider": provider,
                "text": answer,
                "is_fallback": False
            }
        except Exception as e:
            # En cas d'erreur de clé ou réseau
            return {
                "status": "error",
                "provider": provider,
                "text": (
                    f"⚠️ **Une erreur est survenue lors de l'appel à l'API {provider.upper()} :**\n\n"
                    f"`{str(e)}`\n\n"
                    f"Vérifiez que votre clé API est valide et dispose des droits nécessaires.\n\n"
                    f"---\n"
                    f"### 📍 Informations trouvées dans la base Nantes Métropole :\n"
                    + "\n\n".join([f"**{s.get('title')}**\n{s.get('content')}" for s in sources[:2]])
                ),
                "is_fallback": True
            }

llm_service = LLMService()

