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
            agent any
            steps {
                sh 'docker build -t khatangatao/django-locallibrary-tutorial:latest .'
                sh 'echo Docker image khatangatao/django-locallibrary-tutorial:latest done'
            }
        }
    }
}