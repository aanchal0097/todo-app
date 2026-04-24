pipeline{
    agent any 

    environment {
        IMAGE_NAME = "sharmaanchal01/todo-app"
    }
    stages{
        stage{
            steps('Build'){
                echo "Building"
            }
        }
        stage{
            steps('Test'){
                echo "Skipping the test"
            }
        }
        stage{
            steps('Docker Build'){
                sh 'docker build -t sharmaanchal01/todo-app .'
            }
        }
        stage{
            steps('Docker Push'){
                sh 'docker push sharmaanchal01/todo-app'
            }
        }
    }
}