pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('test') {
            steps {
                sh 'cat README.md'
            }

        }

        stage('deploy') {
            steps {
                sh 'echo Deploying...'
            }
        }
    }
}
