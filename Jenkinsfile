pipeline {

    agent {label "First"}

    stages {

        stage ("Git Clone") {
            steps {
                git url: "https://github.com/devopsof/major_project_1.git", branch: "main"
            }
        }

        stage ("Build Docker Image") {
            steps {
                sh '''
                docker build -t flask-app app/.
                '''
            }
        }

        stage ("Test Run") {
            steps {
                sh '''
                docker run -d --name flask-test flask-app
                sleep 5
                docker exec flask-test curl -f http://localhost:5000 || exit 1
                docker rm -f flask-test
                '''
            }
        }

        stage ("Push to Dockerhub") {
            steps {
                sh'''
                docker push irady/flask-app:latest
                '''
            }
        }

        stage ("Deploy Application") {
            steps {
                sh'''
                docker compose up --build
                '''
            }
        }
    }
}