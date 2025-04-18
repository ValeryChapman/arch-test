DOCKER_COMPOSE_LOCAL_PATH=./docker/docker-compose.local.yml
ENV_FILE=.env

build:
	docker compose -f $(DOCKER_COMPOSE_LOCAL_PATH) --env-file $(ENV_FILE) --build

up:
	docker compose -f $(DOCKER_COMPOSE_LOCAL_PATH) --env-file $(ENV_FILE) up

start:
	docker compose -f $(DOCKER_COMPOSE_LOCAL_PATH) --env-file $(ENV_FILE) up --build

postgres:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL_PATH) --env-file $(ENV_FILE) up --build postgres
