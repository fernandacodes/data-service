#!/bin/bash

# Exibir mensagem de início do script
echo "Iniciando o processo de atualização e reinício dos containers..."

# Atualizar o repositório local com o código mais recente
echo "Atualizando o código com git pull..."
git pull origin || { echo "Erro ao executar git pull. Verifique o repositório."; exit 1; }

# Parar os containers
echo "Parando os containers..."
sudo docker compose stop data-service-web-1 data-service-app-1 data-service-nginx-1 || {
  echo "Erro ao parar os containers. Verifique o estado do Docker."; exit 1;
}

# Aguardar os containers pararem completamente
echo "Aguardando containers pararem..."
while sudo docker ps | grep -qE 'data-service-(web|app|nginx)-1'; do
  sleep 2
done

# Remover os containers
echo "Removendo os containers..."
sudo docker rm data-service-web-1 data-service-app-1 data-service-nginx-1 || {
  echo "Erro ao remover os containers. Verifique se eles já estão removidos."; exit 1;
}

# Remover as imagens
echo "Removendo as imagens..."
sudo docker rmi data-service-app nginx data-service-web || {
  echo "Erro ao remover as imagens. Verifique se elas já foram removidas."; exit 1;
}

# Subir os containers (app)
echo "Subindo o container do app..."
sudo docker compose up app -d || { echo "Erro ao subir o container do app."; exit 1; }

# Subir os containers (web)
echo "Subindo o container da web..."
sudo docker compose up web -d || { echo "Erro ao subir o container da web."; exit 1; }

# Subir o nginx por último
echo "Subindo o container do nginx..."
sudo docker compose up nginx -d || { echo "Erro ao subir o container do nginx."; exit 1; }

# Finalização
echo "Processo de atualização e reinício concluído com sucesso!"
