
pipeline {
    agent any
environment { 
        DOCKER_HUB_REPO    = "salmanilyas/flask_image}"
        IMAGE_TAG   = "v3"
    }
    stages {
        stage('Build') {
            steps {
                echo  " Building ${env.BUILD_ID}" 
                sh 'docker build . -t $DOCKER_HUB_REPO:$IMAGE_TAG'
                sh 'docker push $DOCKER_HUB_REPO:$IMAGE_TAG'
                echo 'image is build and push'
            }
        }
        stage('Test') {
            steps {
                  
                 echo "Testing.. ${env.JOB_NAME}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
