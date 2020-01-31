
pipeline {
    agent any
environment { 
        DOCKER_HUB_REPO    = "salmanilyas/flask_image"
        IMAGE_TAG   = "v6"
    }
    stages {
        stage('Config') {
            steps {
                echo 'replacing value in config file'
                sh "sed -i 's@<MONGO_CLIENT_IP>@$MONGO_CLIENT_IP@g' flask_docker/config.py"
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
                sh 'docker run -d --name flask_contianer -p 9091:5011 salmanilyas/flask_image:v6'
                sh 'docker run -d --name mongo_container -p 27017:27017 mongo'
            }
        }
    }
}
