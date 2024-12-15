stop:
	sudo docker stop data-service-app-1
	sudo docker stop data-service-web-1
	sudo docker stop data-service-nginx-1
remove:
	sudo docker rm data-service-app-1
	sudo docker rm data-service-web-1
	sudo docker rm data-service-nginx-1
remove-i:
	sudo docker rmi data-service-app
	sudo docker rmi data-service-web
	sudo docker rmi data-service-nginx
start:
	sudo docker compose up app -d
	sudo docker compose up web -d
	sudo docker compose up nginx -d
deploy:
	git pull origin 
	make stop
	make remove
	make remove-i
	make start
