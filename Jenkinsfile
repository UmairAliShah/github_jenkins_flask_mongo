
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo  " Building ${env.BUILD_ID}" 
                sh 'docker build . -t salmanilyas/flask_image:v2'
                sh 'docker push salmanilyas/flask_image:v2'
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
