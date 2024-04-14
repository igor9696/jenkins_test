pipeline {
    agent {docker {image 'jenkins/jenkins:lts-jdk17'}}
    stages {
        stage('build') {
            steps {
                sh 'python3 jsonParser.py'
            }
        }
    }
}
