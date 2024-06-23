dev:
	docker compose up db -d
	docker compose up web
dbclean:
	docker stop data-service-db-1
	docker rm data-service-db-1
	docker volume rm data-service_postgres_data
webclean:
	docker rm data-service-web-1
	docker rmi data-service-web
db:
	docker compose up db -d
web:
	docker compose up web
