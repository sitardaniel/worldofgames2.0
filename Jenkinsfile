pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'sitardaniel/worldofgames'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Code Quality') {
            parallel {
                stage('Lint') {
                    steps {
                        sh 'flake8 --max-line-length=120 --exclude=venv,__pycache__ .'
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'bandit -r . -x ./venv,./tests --severity-level medium'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/ -v --cov=. --cov-report=xml --cov-report=html --cov-fail-under=50'
            }
            post {
                always {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker-compose up -d'
                // Wait for container to be healthy
                sh 'sleep 10'
            }
        }

        stage('E2E Tests') {
            steps {
                sh 'python3 e2e.py'
            }
        }

        stage('Push to Registry') {
            when {
                branch 'main'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            when {
                branch 'main'
            }
            steps {
                sh "kubectl set image deployment/worldofgames worldofgames=${DOCKER_IMAGE}:${DOCKER_TAG}"
                sh 'kubectl rollout status deployment/worldofgames --timeout=60s'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down || true'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
            // Add Slack/Email notification here
        }
    }
}
