#!/bin/bash
echo "Criando imagens docker e iniciando os containers."
docker-compose build
docker-compose down
docker-compose up -d

timeout=100

for ((i=timeout; i>=0; i--)); do
    clear
    echo "Aguardando servico MySQL - $i segundos"
    sleep 1
done
docker exec -i mysql-container mysql -uroot -pmypassword123 < api/db/script.sql
