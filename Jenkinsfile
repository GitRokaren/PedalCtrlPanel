/* 
Authors: Jonatan Ryd & Jeffrey Persson
Date: 2021-05-04
Test: Running a python program to act as a control panel for robotframework pedal test on RaspberryPi 
*/
pipeline {
    agent any 
    stages {
        // Connecting GitHub to user email
        stage('Connect GitHub') {
            steps {
                echo 'Run the security check against the application' 
                sh "git config --global user.email jeffes159@gmail.com"
            }
        }
        // Run the test
        stage('Run Unit Tests') {
            steps {
                sh "ls"
                dir("${WORKSPACE}"){
                    sh "ls"
                    //sh "python -m robot GPIOPedal.robot"
                }

            }
        }
    }
}
