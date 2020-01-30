
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..' + str(${env.BUILD_ID})
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..' + str(${env.JOB_NAME})
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
