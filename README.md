# CI/CD Pipeline with GitHub Actions & Docker

## Objective
Automate build, test, and deployment of a Dockerized app using GitHub Actions and Docker Hub.

## Tools
GitHub Actions, Docker, Docker Hub, Minikube/Local VM

## Workflow
1. Push code to GitHub → GitHub Actions runs.  
2. Actions: checkout, run tests, build Docker image, push to Docker Hub.  
3. Local VM/Minikube pulls image and runs the container.  

## Deliverables
- **GitHub Repo**: Contains `Dockerfile`, `docker-compose.yml`, `.github/workflows/ci-cd.yml`  
- **Docker Image Link**: `docker.io/parth123/myapp:latest`  
- **CI/CD Workflow Results**: Logs show ✅ tests, ✅ build, ✅ push, ✅ deploy  
- **Screenshots**:  
  - GitHub Actions success (green check)  
  - Docker Hub with latest image  
  - `docker ps` output showing app running  
  - Browser view of `http://localhost:8080`  

## Folder Structure
myapp/  
├── Dockerfile  
├── docker-compose.yml  
├── app/ (sample app code, e.g. `main.py`)  
├── tests/ (sample tests, e.g. `test_app.py`)  
└── .github/workflows/ci-cd.yml  

## Notes
- App runs on port 8080.  
- Pipeline triggers on push to `main`.  
- Image automatically pushed to Docker Hub and pulled locally for deployment.  
