# FastAPI Template
This is a starter project for Python that includes a sample REST API implementation using FastAPI, and a sample database access implementation using hexagonal architecture. It also includes linting and testing tools to help you develop high-quality code.

## Purpose
The purpose of this project is to provide a starting point for building Python applications. It includes a sample implementation of a REST API using the FastAPI framework, which makes it easy to build web applications quickly and efficiently. It also includes a sample implementation of database access using hexagonal architecture, which provides a clean separation between the application logic and the database implementation. This makes it easy to switch between different database technologies without affecting the application code.

## Features
This starter project includes the following features:

- A sample implementation of a REST API using FastAPI
- A sample implementation of database access using hexagonal architecture
- Linting tools (flake8, pylint) to ensure consistent code style
- Testing tools (pytest) to help you write reliable and maintainable code
- Dockerfiles for local development, AWS EKS, and AWS Lambda

## Getting Started
To get started with this project, follow these steps:

- Clone this repository to your local machine.
- Install the dependencies using Poetry.
```
poetry install
```

- run the development server using:

```
./run-dev.sh 
```

This will start the container and forward port 8000 on your local machine to port 8000 inside the container. You can access the app at http://localhost:8000/.

## Running Tests
This project includes unit tests to ensure that the code is working correctly. To run the tests, use the following command:

```
pytest
docker exec -it fastapi-template-main-app-1 pytest
```

## Linting
This project includes linting tools to ensure that the code is consistent and easy to read. To run the linters, use the following command:

```
poetry run flake8 app
poetry run pylint app
```


## AWS EKS
The Dockerfile.k8s file is designed for running the app inside an AWS EKS cluster. To use it, you'll need to build the image and push it to a container registry that's accessible from your EKS cluster.

```
docker build -t my-docker-registry/myproject:latest -f Dockerfile .
docker push my-docker-registry/myproject:latest
```

Replace my-docker-registry with the name of your container registry.

Then, you'll need to deploy the Kubernetes deployment file to your EKS cluster:

```
kubectl apply -f docker-deployment.k8.yaml
```
This will create a Kubernetes deployment for the app.


## AWS Lambda

The Dockerfile.lambda file is designed for running the app inside an AWS Lambda container. To use it, you'll need to build the image and push it to a container registry that's accessible from AWS Lambda.

Build the Docker image for AWS Lambda:
```
docker build -t my-docker-registry/myproject:latest -f Dockerfile.lambda .
```
Replace my-docker-registry with the name of your container registry.

```
docker push my-docker-registry/myproject:latest
```