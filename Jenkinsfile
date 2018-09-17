pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }
    stages {
        stage('build') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh 'cat README.md'
            }
        }

        stage('test') {
            agent {
                dockerfile {
                    filename 'Dockerfile'
                }
            }
            steps {
                sh './manage.py test'
            }

        }

        stage('delivery') {
            agent none
            steps {
                sh 'docker build -t khatangatao/django-locallibrary-tutorial:latest .'
                sh 'docker login'
                sh 'docker push khatangatao/django-locallibrary-tutorial:latest'
            }
        }
    }
}