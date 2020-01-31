
pipeline {
    agent any
environment { 
        DOCKER_HUB_REPO    = "salmanilyas/flask_image"
        IMAGE_TAG   = "v4"
    }
    stages {
        stage('Config') {
            steps {
                echo 'replacing value in config file'
                sh "sed -i 's@<MONGOG_CLIENT_IP>@$MONGOG_CLIENT_IP@g' flask_docker/config.py"
                sh "sed -i 's@<MONGO_PORT>@$MONGO_PORT@g' flask_docker/config.py"
                sh 'cat flask_docker/config.py'
               
            }
        }
        stage('Build') {
            steps { 
                echo  " Building ${env.BUILD_ID}" 
                sh 'docker build . -t $DOCKER_HUB_REPO:$IMAGE_TAG'
                sh 'docker push $DOCKER_HUB_REPO:$IMAGE_TAG'
                echo 'image is build and push'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}