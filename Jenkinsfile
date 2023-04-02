pipeline {
    agent any
    environment {
        APP_NAME = 'clock-app'
        DOCKERHUB_REGISTRY = 'docker.io'
        DOCKERHUB_REPOSITORY = 'ryankim5100/testjenkins'
        K8S_NAMESPACE = 'default'
        K8S_DEPLOYMENT_NAME = 'clock-app-deployment'
        K8S_SERVICE_NAME = 'clock-app-service'
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }
    stages {
        stage('Source Checkout') {
            steps {
                git 'https://github.com/ryan-kim21/Test-build-23-04.git'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$BUILD_NUMBER .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh 'docker login --username my-dockerhub-account --password my-dockerhub-password'
                sh 'docker push $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$BUILD_NUMBER'
            }
        }
        stage('Kubernetes Deployment') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml -n $K8S_NAMESPACE'
                sh 'kubectl apply -f k8s/service.yaml -n $K8S_NAMESPACE'
            }
        }
    }
}