#!/bin/bash

DATA=$(date +"%d-%m-%Y")

echo "Atualizando repositorio remoto..."
git pull origin main

# Verifica se há alterações
git diff --quiet
if [ $? -eq 0 ]; then
    echo "Nenhuma alteracao para commit."
    read -p "Pressione ENTER para sair..."
    exit 0
fi

git add .
git commit -m "Atualizacao $DATA"
git push origin main

# TESTE
