pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                    dir 'build'
                }
            }
            steps {
                sh 'python --version'
            }


        }
    }
}
