# Makefile para atualização de containers Docker

# Variáveis
WEB_CONTAINER = data-service-web-1
APP_CONTAINER = data-service-app-1
NGINX_CONTAINER = data-service-nginx-1
WEB_IMAGE = data-service-web
APP_IMAGE = data-service-app
NGINX_IMAGE = nginx

# Função para exibir mensagens com timestamp
define log_message
	@echo "[$(shell date '+%Y-%m-%d %H:%M:%S')] $1"
endef

# Alvo principal: atualizar containers
update: stop remove_images start
	$(call log_message, "Processo de atualização concluído com sucesso!")

# Parar os containers
stop:
	$(call log_message, "Parando o container web...")
	@sudo docker compose stop $(WEB_CONTAINER) || $(call log_message, "Falha ao parar o container web.")
	$(call log_message, "Parando o container app...")
	@sudo docker compose stop $(APP_CONTAINER) || $(call log_message, "Falha ao parar o container app.")
	$(call log_message, "Parando o container nginx...")
	@sudo docker compose stop $(NGINX_CONTAINER) || $(call log_message, "Falha ao parar o container nginx.")
	$(call log_message, "Aguardando os containers pararem...")
	@while sudo docker ps | grep -qE 'data-service-(web|app|nginx)-1'; do sleep 3; done
	$(call log_message, "Containers parados com sucesso.")

# Remover os containers
remove:
	$(call log_message, "Removendo o container web...")
	@sudo docker rm $(WEB_CONTAINER) || $(call log_message, "Falha ao remover o container web.")
	$(call log_message, "Removendo o container app...")
	@sudo docker rm $(APP_CONTAINER) || $(call log_message, "Falha ao remover o container app.")
	$(call log_message, "Removendo o container nginx...")
	@sudo docker rm $(NGINX_CONTAINER) || $(call log_message, "Falha ao remover o container nginx.")

# Remover as imagens
remove_images:
	$(call log_message, "Removendo as imagens...")
	@sudo docker rmi $(WEB_IMAGE) $(APP_IMAGE) $(NGINX_IMAGE) || $(call log_message, "Falha ao remover algumas imagens. Verifique manualmente.")

# Subir os containers
start:
	$(call log_message, "Subindo o container app...")
	@sudo docker compose up app -d || { $(call log_message, "Erro ao subir o container app."); exit 1; }
	$(call log_message, "Subindo o container web...")
	@sudo docker compose up web -d || { $(call log_message, "Erro ao subir o container web."); exit 1; }
	$(call log_message, "Subindo o container nginx...")
	@sudo docker compose up nginx -d || { $(call log_message, "Erro ao subir o container nginx."); exit 1; }

