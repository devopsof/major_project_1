# Flask App with CI/CD 🚀

This is a simple Flask web application deployed using **Docker Compose** and built automatically with **Jenkins**.

## How it works
- The app is a small Python/Flask service.
- Code is stored in GitHub.
- Jenkins pipeline builds the Docker image, pushes it, and deploys using `docker-compose`.
- Docker Compose runs the container locally or on your server.

## Project Structure
