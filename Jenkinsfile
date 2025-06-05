pipeline {
    agent any

    environment {
        IMAGE_NAME = 'todopy-app'
        CONTAINER_NAME = 'todopy-test'
        NEXUS_URL = '172.19.0.3:8082'
        NEXUS_REPO = 'docker_labs'
        VERSION = '1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/chagasgb/todopy.git', 
                    branch: 'main',
                    credentialsId: 'HTTP_GITHUB'
            }
        }

        stage('Build Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm --name $CONTAINER_NAME $IMAGE_NAME pytest tests/test.py"
                }
            }
        }

        stage('Push artifacts to Nexus') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'NEXUS_HTTP', usernameVariable: 'NEXUS_USER', passwordVariable: 'NEXUS_PASS')]) {
                    script {
                        sh """
                            echo "$NEXUS_PASS" | docker login $NEXUS_URL --username "$NEXUS_USER" --password-stdin
                            docker tag $IMAGE_NAME $NEXUS_URL/$NEXUS_REPO/$IMAGE_NAME:$VERSION
                            docker push $NEXUS_URL/$NEXUS_REPO/$IMAGE_NAME:$VERSION
                        """
                    }
                }
            }
        }
    }
}
