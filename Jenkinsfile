
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..' + env.BUILD_ID
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..' + env.JOB_NAME
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
