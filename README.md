# roche-shopping-cart
Backend services for Roche Shopping Cart

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://black.readthedocs.io/en/stable/)
[![Typed with: pydantic](https://img.shields.io/badge/typed%20with-pydantic-BA600F.svg?style=for-the-badge)](https://docs.pydantic.dev/)


## Development

Requirements:
  - [docker](https://www.docker.com/)
  - [docker-compose](https://docs.docker.com/compose/)
  - [make](https://www.gnu.org/software/make/manual/html_node/Introduction.html)

### Setup

```bash
git clone https://github.com/liman4u/roche-shopping-cart.git

cd roche-shopping-cart

cp .env-example .env

make setup
```

### Run API
```bash

make run-api
```

### Run Test
```bash

make test
```


## API

Available API [docs](http://localhost:8000/docs)


| Method | Endpoint                      | Description                                                                  |
| ------ | ----------------------------- | -----------------------------------------------------------------------------|
| GET    | /api/v1/health                 | Check if service is healthy                                                  |
| POST   | /api/v1/shopping_cart_item | Add item to shopping cart call reservation service to run in the background for reserving cart item                         |
| GET    | /api/v1/shopping_cart_item                      | Get all cart items                                           |

![Swagger UI](swagger_ui.png)

# Dependencies

- FastAPI - Writing restful api(requests and responses)

- Pytest - Writing tests

- Coverage - Checking coverage of code tested

- Flake8 - Combines pep8 and pyflakes for linting

- Black - Great tool for formatting

- Dependency Injector - Managing and injection of initialised service and repository

- Structlog - Logging

- AIOHttp - Making client calls


## What more can be done.
1. User authentication and authorization to protect routes
2. Pagination when getting all shopping cart items to limit data size
3. Rate limiting for the APIs to prevent attack like DDOS
4. Integration Tests to test API with external service
5. Making use of Celery for long running background task
6. Dockerfile for production and CI/CD workflows for building and deployment of docker images.
7. Sufficient unit tests
8. Fixing of `emit_reserve_cart_item` unit tests, marked with x_, so it does not run - was getting issue with host of wiremock in test

## References
1. [FastAPI official docs](https://fastapi.tiangolo.com/)
2. [Dependency Injector](https://python-dependency-injector.ets-labs.org/)
3. [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
