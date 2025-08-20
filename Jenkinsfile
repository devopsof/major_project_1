pipeline {

    agent {label "First"}

    environment {

        IMAGE_NAME = "flask-app"
        IMAGE_TAG = "latest"

    }

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

        stage('Test Run') {
            steps {
                sh '''
                docker rm -f flask-test || true
                docker run -d --name flask-test -p 5000:5000 flask-app
                sleep 5
                curl -f http://localhost:5000 || exit 1
                docker rm -f flask-test
                '''
            }
        }


        stage("Push to Dockerhub") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        docker logout
                    '''
                }
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