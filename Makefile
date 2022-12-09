DOCKER_BASH=docker exec -it organizer-auth
MANAGE=python3 manage.py

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

rebuild: down build up

bash:
	${DOCKER_BASH} bash

restart: down up

show-routes:
	${DOCKER_BASH} ${MANAGE} show_urls
