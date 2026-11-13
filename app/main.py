"""
Application principale FastAPI pour le Chatbot Nantes Métropole.
Fournit l'API RAG + LLM et sert l'interface utilisateur web moderne.
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv, set_key

# Charger les variables d'environnement depuis .env
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

from app.knowledge_data import get_categories, get_all_chunks
from app.rag_engine import rag_engine
from app.llm_service import llm_service

app = FastAPI(
    title="Nantes Métropole Chatbot IA",
    description="Assistant intelligent RAG pour les transports, hôtels et lieux historiques de Nantes",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Répertoires
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Modèles Pydantic pour la validation
class ChatTurn(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatTurn]] = []
    provider: Optional[str] = "gemini"  # "gemini" ou "openai"
    api_key: Optional[str] = None

class KeyConfigPayload(BaseModel):
    provider: str
    api_key: str

class TestKeyPayload(BaseModel):
    provider: str
    api_key: str

class FeedbackPayload(BaseModel):
    message_id: Optional[str] = None
    rating: str  # "up" ou "down"
    comment: Optional[str] = None

@app.get("/")
async def get_index(request: Request):
    """Page d'accueil de l'interface du chatbot."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"title": "Naomì - Assistant Nantes Métropole"}
    )

@app.get("/api/categories")
async def api_categories():
    """Retourne la liste des thématiques prises en charge."""
    return {"categories": get_categories()}

@app.post("/api/feedback")
async def api_feedback(payload: FeedbackPayload):
    """Enregistre le retour utilisateur (pouce haut / pouce bas)."""
    return {"status": "ok", "message": "Merci pour votre retour !"}

@app.post("/api/config/test")
async def api_test_key(payload: TestKeyPayload):
    """Teste la validité d'une clé API en effectuant un appel minimal."""
    key = payload.api_key.strip()
    if not key or len(key) < 8:
        raise HTTPException(status_code=400, detail="Clé trop courte ou vide.")
    
    try:
        if payload.provider == "openai":
            import requests
            res = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5},
                timeout=10
            )
            if res.status_code == 200:
                return {"valid": True, "message": "Connexion OpenAI réussie (GPT-4o-mini prêt) !"}
            else:
                err = res.json().get("error", {}).get("message", res.text)
                return {"valid": False, "message": f"Erreur OpenAI : {err}"}
        else:
            # Gemini
            import requests
            model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
            res = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
                json={"contents": [{"parts": [{"text": "ping"}]}], "generationConfig": {"maxOutputTokens": 5}},
                timeout=10
            )
            if res.status_code == 200:
                return {"valid": True, "message": f"Connexion Google Gemini réussie ({model} prêt) !"}
            else:
                err = res.json().get("error", {}).get("message", res.text)
                return {"valid": False, "message": f"Erreur Gemini : {err}"}
    except Exception as e:
        return {"valid": False, "message": f"Échec de connexion : {str(e)}"}

@app.get("/api/suggestions")
async def api_suggestions():
    """Retourne des suggestions de questions types pour Nantes."""
    return {
        "suggestions": [
            {
                "category": "transports",
                "label": "Transports gratuits le week-end ?",
                "prompt": "Est-ce que les transports sont vraiment gratuits le week-end à Nantes et comment ça marche ?"
            },
            {
                "category": "transports",
                "label": "Comment aller à l'aéroport ?",
                "prompt": "Quel est le meilleur moyen pour aller du centre de Nantes à l'aéroport Nantes Atlantique ?"
            },
            {
                "category": "patrimoine",
                "label": "Visiter les Machines de l'Île",
                "prompt": "Que voir aux Machines de l'Île et comment fonctionne le Grand Éléphant ?"
            },
            {
                "category": "patrimoine",
                "label": "Le Château des ducs de Bretagne",
                "prompt": "Peut-on visiter les remparts du Château des ducs de Bretagne gratuitement et que trouve-t-on à l'intérieur ?"
            },
            {
                "category": "hotels",
                "label": "Où loger pour visiter à pied ?",
                "prompt": "Quel quartier me conseilles-tu pour réserver un hôtel afin de tout visiter à pied à Nantes ?"
            },
            {
                "category": "hotels",
                "label": "Un hôtel insolite ou de charme",
                "prompt": "Recommande-moi un hôtel de charme ou atypique à Nantes pour un week-end en amoureux."
            },
            {
                "category": "gastronomie",
                "label": "Spécialités culinaires nantaises",
                "prompt": "Quelles sont les spécialités gourmandes typiques de Nantes et où déguster un bon gâteau nantais ?"
            },
            {
                "category": "pratique",
                "label": "Que faire en 1 ou 2 jours ?",
                "prompt": "J'ai 2 jours pour visiter Nantes avec des amis, quel itinéraire nous recommandes-tu ?"
            }
        ]
    }

@app.get("/api/config")
async def api_config():
    """Indique l'état de configuration des clés API (sans révéler le secret)."""
    gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    return {
        "gemini_configured": bool(gemini_key and len(gemini_key) > 5),
        "openai_configured": bool(openai_key and len(openai_key) > 5),
        "default_provider": "gemini" if gemini_key else ("openai" if openai_key else "gemini")
    }

@app.post("/api/config/save")
async def api_save_key(payload: KeyConfigPayload):
    """Enregistre la clé API dans le fichier .env."""
    if not payload.api_key or len(payload.api_key.strip()) < 8:
        raise HTTPException(status_code=400, detail="Clé API invalide ou trop courte.")

    env_file = BASE_DIR / ".env"
    if not env_file.exists():
        env_file.touch()

    key_name = "OPENAI_API_KEY" if payload.provider == "openai" else "GEMINI_API_KEY"
    set_key(str(env_file), key_name, payload.api_key.strip())
    os.environ[key_name] = payload.api_key.strip()

    return {"status": "success", "message": f"Clé {key_name} configurée avec succès !"}

@app.post("/api/chat")
async def api_chat(payload: ChatRequest):
    """Point d'entrée principal pour discuter avec le Chatbot RAG."""
    query = payload.message.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Le message ne peut pas être vide.")

    # 1. Étape RAG : Recherche documentaire ciblée sur Nantes
    retrieved_chunks = rag_engine.search(query, top_k=3)
    rag_context = rag_engine.build_rag_context(retrieved_chunks)

    # 2. Conversion historique
    history_dicts = [{"role": t.role, "content": t.content} for t in (payload.history or [])]

    # 3. Étape LLM : Génération de la réponse avec le prompt enrichi
    generation = llm_service.generate_response(
        message=query,
        rag_context=rag_context,
        sources=retrieved_chunks,
        history=history_dicts,
        provider=payload.provider or "gemini",
        user_key=payload.api_key
    )

    # 4. Formater les sources retournées au client
    formatted_sources = [
        {
            "id": c.get("id"),
            "category": c.get("category"),
            "title": c.get("title"),
            "content": c.get("content")
        }
        for c in retrieved_chunks
    ]

    return {
        "status": generation.get("status"),
        "reply": generation.get("text"),
        "provider": generation.get("provider"),
        "is_fallback": generation.get("is_fallback", False),
        "sources": formatted_sources
    }
