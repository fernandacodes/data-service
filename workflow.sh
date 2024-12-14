#!/bin/bash

# Exibir mensagem de início do script
echo "Iniciando o processo de atualização e reinício dos containers..."

# Parar os containers
echo "Parando os containers..."
sudo docker compose stop data-service-web-1 data-service-app-1 data-service-nginx-1

# Remover os containers
echo "Removendo os containers..."
sudo docker rm data-service-web-1 data-service-app-1 data-service-nginx-1

# Remover as imagens
echo "Removendo as imagens..."
sudo docker rmi data-service-app nginx data-service-web

# Subir os containers (app)
echo "Subindo o container do app..."
sudo docker compose up app -d

# Subir os containers (web)
echo "Subindo o container da web..."
sudo docker compose up web -d

# Subir o nginx por último
echo "Subindo o container do nginx..."
sudo docker compose up nginx -d

# Finalização
echo "Processo de atualização e reinício concluído com sucesso!"
