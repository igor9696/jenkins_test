pipeline {
    agent {docker {image 'python:alpine3.18'}}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}
