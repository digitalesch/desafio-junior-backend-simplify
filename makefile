build:
	docker build . -t micro_python:1.0.0

up:
	docker compose -f docker-compose.yml up

down:
	docker compose -f docker-compose.yml down && docker-compose rm -fsv