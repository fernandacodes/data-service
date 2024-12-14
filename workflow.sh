#!/bin/bash

# Função para exibir mensagens com timestamp
log_message() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log_message "Iniciando o processo de atualização..."

# 1. Parar os containers individualmente
log_message "Parando o container web..."
sudo docker compose stop data-service-web-1 || log_message "Falha ao parar o container web."

log_message "Parando o container app..."
sudo docker compose stop data-service-app-1 || log_message "Falha ao parar o container app."

log_message "Parando o container nginx..."
sudo docker compose stop data-service-nginx-1 || log_message "Falha ao parar o container nginx."

# 2. Aguardar os containers pararem completamente
log_message "Aguardando os containers pararem..."
while sudo docker ps | grep -qE 'data-service-(web|app|nginx)-1'; do
  sleep 3
done
log_message "Containers parados com sucesso."

# 3. Remover os containers individualmente
log_message "Removendo o container web..."
sudo docker rm data-service-web-1 || log_message "Falha ao remover o container web."

log_message "Removendo o container app..."
sudo docker rm data-service-app-1 || log_message "Falha ao remover o container app."

log_message "Removendo o container nginx..."
sudo docker rm data-service-nginx-1 || log_message "Falha ao remover o container nginx."

# 4. Remover as imagens
log_message "Removendo as imagens..."
sudo docker rmi data-service-web data-service-app nginx || log_message "Falha ao remover algumas imagens. Verifique manualmente."

# 5. Subir os containers individualmente
log_message "Subindo o container app..."
sudo docker compose up app -d || { log_message "Erro ao subir o container app."; exit 1; }

log_message "Subindo o container web..."
sudo docker compose up web -d || { log_message "Erro ao subir o container web."; exit 1; }

log_message "Subindo o container nginx..."
sudo docker compose up nginx -d || { log_message "Erro ao subir o container nginx."; exit 1; }

log_message "Processo de atualização concluído com sucesso!"
