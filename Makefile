# Build configuration
BUILD_DIR ?= build/
DC := docker-compose

# Other config
NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m

.PHONY: build-images run-dependencies

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run        			to run the service"
	@echo "  stop       			to stop docker containers"
	@echo "  down       			to spin down docker containers"
	@echo "  setup                	to build the docker images and run dependencies"
	@echo "  build-images           to build docker images"
	@echo "  run-dependencies       to run only the dependencies: database"
	@echo "  clean      			to clean docker resources"


setup: clean build-images run-dependencies

build-images:
	$(DC) build

run-api:
	$(DC) up -d api

run-dependencies:
	$(DC) up -d database reservation-service
	sleep 3

stop:
	$(DC) stop

down:
	$(DC) down

clean:
	$(DC) down -v --rmi local --remove-orphans

test:
	python -m pytest --disable-warnings -v --cov=./ --cov-report=xml  tests/ 
