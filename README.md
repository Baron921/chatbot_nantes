# Naomì • Chatbot IA & RAG pour Nantes Métropole

Assistant conversationnel intelligent pour les résidents, touristes et visiteurs de **Nantes Métropole**. Il répond de manière ultra-pertinente et sourcée aux questions sur les **transports (réseau Naolib)**, les **hôtels**, le **patrimoine historique**, la **gastronomie** et les **bons plans**.

---

## Fonctionnalités Clés

- ** Architecture 100% IA Générative avec RAG (Retrieval-Augmented Generation) :**
  - Moteur d'indexation et de recherche documentaire local avec **SQLite FTS5** (ranking BM25 + pertinence thématique).
  - Injection dynamique du contexte documentaire certifié de Nantes dans le prompt de l'IA pour éliminer les hallucinations et garantir des faits exacts.
  - Support de **Google Gemini** (`gemini-2.5-flash` / API gratuite sur Google AI Studio) et **OpenAI** (`gpt-4o-mini`).
- ** Transparence des Sources (RAG) :**
  - Chaque réponse affiche les sources de connaissances exactes consultées (collapsibles sous le message).
- ** Connaissances Spécifiques sur Nantes Métropole :**
  - **Transports Naolib :** Gratuité totale de tous les transports le **week-end** (samedi et dimanche), lignes de tramway 1, 2, 3, Busway 4 et 5, Navibus Loire (Gare Maritime ↔ Trentemoult) et Erdre, vélos Bicloo, accès aéroport Nantes Atlantique en navette ou bus.
  - **Patrimoine & Culture :** Château des ducs de Bretagne (remparts gratuits), Les Machines de l'Île (Grand Éléphant, Carrousel des Mondes Marins), Passage Pommeraye, Jardin des Plantes, Cathédrale Saint-Pierre, Le Voyage à Nantes (Ligne Verte), village pittoresque de Trentemoult, Tour LU / Lieu Unique, Musée d'Arts, Hangar à Bananes & Anneaux de Buren.
  - **Hôtels & Hébergements :** Recommandations par quartier (Graslin/Centre piéton, Gare SNCF/Cité des Congrès, Île de Nantes) et par budget (luxe, insolite comme le Sozo Hôtel dans une chapelle, confort Novotel/Mercure, économique comme l'Auberge HI La Manu).
  - **Gastronomie nantaise :** Gâteau nantais au rhum, Muscadet, fromage Le Curé Nantais, Beurre Blanc, Berlingots & Rigolettes, Marché de Talensac, brasserie La Cigale.
- ** Interface Web Responsive & Moderne :**
  - Design inspiré de l'identité de Nantes Métropole (Tailwind CSS, Lucide Icons, Marked.js).
  - Suggestions de questions en 1 clic.
  - Synthèse vocale intégrée (Web Speech API) avec voix française pour écouter les réponses.
  - Bouton de copie rapide.
  - Modale de configuration de clé API directement dans l'interface (avec persistance optionnelle dans `.env`).

---

## Démarrage Rapide

### 1. Prérequis
- Python 3.10 ou supérieur (Python 3.14 installé).

### 2. Lancement du serveur

Exécutez simplement le script de démarrage à la racine :

```bash
./run.sh
```

Ou manuellement via uvicorn :

```bash
# Activation de l'environnement virtuel
source venv/bin/activate

# Lancement du serveur FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

Ouvrez ensuite votre navigateur sur : **[http://localhost:3000](http://localhost:3000)**

---

## Configuration des Clés API (Gemini ou OpenAI)

Le chatbot fonctionne avec une clé d'API d'IA générative :

### Option A : Depuis l'interface web (Le plus simple)
1. Ouvrez l'application sur `http://localhost:8080`.
2. Cliquez sur l'icône **⚙️ Clé API / Modèle** en haut à droite.
3. Sélectionnez **Google Gemini** (recommandé) ou **OpenAI**.
4. Collez votre clé API et cochez *"Persister dans le fichier serveur (.env)"*.
5. Cliquez sur **Enregistrer la clé**.

### Option B : Via le fichier `.env`
Éditez le fichier `.env` à la racine :

```env
# Clé Google Gemini (obtenez-en une gratuitement sur https://aistudio.google.com/)
GEMINI_API_KEY=votre_cle_gemini_ici
GEMINI_MODEL=gemini-2.5-flash

# OU Clé OpenAI (https://platform.openai.com/api-keys)
OPENAI_API_KEY=votre_cle_openai_ici
OPENAI_MODEL=gpt-4o-mini
```

---

## Structure du Projet

```text
/opt/lampp/htdocs/chat/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application FastAPI, routes REST et templates
│   ├── rag_engine.py        # Moteur RAG SQLite FTS5 (recherche BM25 + sémantique)
│   ├── llm_service.py       # Intégration Gemini & OpenAI avec prompt système expert
│   └── knowledge_data.py    # Base de connaissances documentaires de Nantes Métropole
├── static/
│   ├── css/
│   │   └── style.css        # Styles typographiques, markdown et animations
│   ├── js/
│   │   └── chat.js          # Client JS (dialogue, audio TTS, RAG, modale)
│   └── img/
│       └── logo.svg         # Logo vectoriel officiel Naomì / Nantes
├── templates/
│   └── index.html           # Interface web responsive Tailwind CSS
├── requirements.txt         # Dépendances Python
├── run.sh                   # Script de lancement automatique
├── .env                     # Variables d'environnement locales
└── README.md
```

---

## Documentation des Endpoints API

FastAPI génère automatiquement la documentation interactive Swagger accessible sur :
**`http://localhost:3000/docs`**

- `POST /api/chat` : Envoi d'un message utilisateur, recherche RAG et génération de réponse LLM.
- `GET /api/categories` : Liste des thématiques nantaises (transports, patrimoine, hôtels, etc.).
- `GET /api/suggestions` : Suggestions de questions fréquentes.
- `GET /api/config` : État de configuration des clés API sur le serveur.
- `POST /api/config/save` : Sauvegarde de la clé API dans le `.env`.
