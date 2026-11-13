#!/usr/bin/env bash
# Script de lancement du Chatbot Nantes Métropole

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "=========================================================="
echo "  🐘 Naomì • Assistant IA Nantes Métropole (RAG + LLM)  "
echo "=========================================================="

# Vérifier l'environnement virtuel
if [ ! -d "venv" ]; then
    echo "Creation de l'environnement virtuel venv..."
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt
fi

PORT="${PORT:-3000}"

echo "Demarrage du serveur sur http://localhost:$PORT ..."
echo "Ouvrez votre navigateur sur : http://localhost:$PORT"
echo "Pour arreter le serveur : Ctrl + C"
echo "=========================================================="

exec ./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port "$PORT" --reload
