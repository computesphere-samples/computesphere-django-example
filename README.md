<p align="right">
    <a href="https://computesphere.com/"><img src="/calculator/static/assets/images/logo.svg" width="50px" /></a>
</p>

# ComputeSphere Django Age Calculator Example App

This example deploys a django application to ComputeSphere.

> [!NOTE]
> This guide builds a Docker image for the provided sample code. Please note that the version `v0.0.1` used in the example is only for demonstration. You should replace it with a version that suits your specific setup and requirements.

## Prerequisites

- A [ComputeSphere](https://computesphere.com) account
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/engine/install/)

## Setup

1. Clone this repository.

   ```bash
   git clone https://github.com/computesphere-samples/computesphere-django-example.git

   cd computesphere-django-example
   ```

2. Create the docker image.

   ```bash
   docker build -t computesphere-django-example:v.0.0.1 .
   ```

   Alternatively, you can use the `docker buildx --build` command to utilize Docker's BuildKit which offers several improvements over the traditional Docker build.

   ```bash
   docker buildx build --platform=linux/amd64 --tag computesphere-django-example:v0.0.1 .
   ```

3. Push the image to Docker Hub.

   ```bash
   docker tag computesphere-django-example:v0.0.1 [REPOSITORY]/computesphere-django-example:v0.0.1

   docker push [REPOSITORY]/computesphere-django-example:v0.0.1
   ```

> [!NOTE]
> Be sure to log in to Docker Hub and replace `[REPOSITORY]` with your Docker Hub username.

## Running the project locally

Run the server locally.

```bash
cd computesphere-django-example

docker run -p 8000:8000 computesphere-django-example:v.0.0.1
```

This runs the server on `localhost:8000`.

## Deploy to ComputeSphere

<!-- Add a link to the blog once published -->

See our [guide](https://docs.computesphere.com/docs/getting-started/quickstart/getting-started-with-django) on how to deploy this project to ComputeSphere.

<!-- Check if this is the right link to the dashboard -->

<a href="https://console.computesphere.com"> <img src="https://cdn.sanity.io/images/5jct4wv7/production/a3a823db7833f9274fc723b1223084b51c7ed160-1103x160.png" width="350px" alt="ComputeSphere Logo"> </a>

---
[Explore ComputeSphere Documentation](https://docs.computesphere.com)

**Contact Us:**  
[support@computesphere.com](mailto:support@computesphere.com)  
[Support Portal](https://support.computesphere.com/portal)

&copy; 2024 ComputeSphere LLC. All Rights Reserved.

---
