# Flask WEB APP vs Tensorflow model Project

This project aims to deploy a Flask web application and TensorFlow Serving model on Kubernetes using Helm charts and Docker containers.

## Project Structure

The project consists of the following components:

- `flask-app`: Contains the Flask web application source code, Dockerfile, and Helm chart for deployment.
- `tf_model`: Contains the TensorFlow Serving model source code, Dockerfile, and Helm chart for deployment.
- `.github/workflows`: Contains GitHub Actions workflows for continuous integration (CI).

## Requirements

To run this project, you need the following:

- Docker
- Kubernetes
- Helm
- TensorFlow
- Locust (for load testing)
- GitHub Actions (for CI)

## Getting Started

To deploy the Flask web application and TensorFlow model on Kubernetes, follow these steps:

1. Build and push the Docker images for both components.
2. Create Helm charts for deployment.
3. Deploy the Helm charts on Kubernetes using Helm.
4. Verify that the services are running correctly.

## Continuous Integration (CI)

The project includes GitHub Actions workflows for CI. The workflows perform the following tasks:

- Building Docker images.
- Pushing Docker images to Docker Hub.