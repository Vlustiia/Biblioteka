pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                cat README.md
            }
        }
    }
}
