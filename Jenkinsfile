pipeline {
    agent any 

    environment {
        IMAGE_NAME = "sharmaanchal01/todo-app"
    }

    stages {

        stage('Build') {
            steps {
                echo "Building"
            }
        }

        stage('Test') {
            steps {
                echo "Skipping the test"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t sharmaanchal01/todo-app .'
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push sharmaanchal01/todo-app'
            }
        }
    }
}