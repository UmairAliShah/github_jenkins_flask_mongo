
pipeline {
    agent any
environment { 
        DOCKER_HUB_REPO    = "salmanilyas/flask_image"
        IMAGE_TAG   = "v100"
    }
    stages {
        stage('Config') {
            steps {
                echo 'replacing value in config file'
                sh "sed -i 's@<MONGO_PORT>@$MONGO_PORT@g' flask_docker/config.py"
                sh 'cat flask_docker/config.py'
               
            }
        }
        stage('Build') {
            steps { 
                echo  " Building ${env.BUILD_ID}" 
                sh 'docker build -t $DOCKER_HUB_REPO:$IMAGE_TAG .'
                sh 'docker push $DOCKER_HUB_REPO:$IMAGE_TAG'
                echo 'image is build and push'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker service create --name flask --replicas 5 --publish 5011:5011 -e mongo=mongo --network my-ingress $DOCKER_HUB_REPO:$IMAGE_TAG'
                sh 'docker service create --name mongo --network my-ingress mongo'
            }
        }
    }
}
