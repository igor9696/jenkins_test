pipeline {
    agent {docker {image 'myjenkins-blueocean:2.440.2-1'}}
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
