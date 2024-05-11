# Comandos
dev:
	docker compose up --build

dev-force:
	docker compose up --force-recreate

stop:
	docker compose down

make-clean:
	docker compose down --rmi all --volumes
