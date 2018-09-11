pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'python --version'
            }


        }
    }
}
