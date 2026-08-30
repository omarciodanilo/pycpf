#!/bin/bash

APP_FILES_AND_FOLDERS="app.py cpf.py __init__.py static/ templates/"

echo -e "(1/2) Compactando arquivos e pastas da aplicação..."
if tar -czf app.tar.gz $APP_FILES_AND_FOLDERS; then
    echo "(2/2) Compactação concluída com sucesso."
else
    echo "(2/2) Erro: A compactação falhou."
fi