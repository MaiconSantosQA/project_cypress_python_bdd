pipeline {
    agent any
 
    environment {
        CI = true
        REPORT_PATH = "allure-results"
        REPORT_NAME = "REPORT.docx"
    }
    stages {
        
        stage('Install requirements') {
            steps {
                dir("bdd"){
                    sh "pip install -r requirements.txt"
                }
            }
        }

    
        stage('Run Features - SMOKE') {
            when {
                expression {env.JOB_NAME == "PDGDI_Smoke_Tests"}
            }
            steps {
                dir("bdd"){
                    script {                
                        try {
                            sh "behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features -f pretty --tags=smoke -k"
                            ignoreFailures=true

                        } catch(err){
                            echo "Testes com falha"
                                        
                        } finally {
                            junit allowEmptyResults: true, testResults: 'reports/*.xml'
                            allure ([
                                includeProperties: false,
                                jdk: '',
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: 'allure-results']],
                            ])
                        }                   
                    }
                }               
            }
        }
        
        stage('Run Features - BUGS') {
            when {
                expression {env.JOB_NAME == "PDGDI_Bugs_Tests"}
            }
            steps {
                dir("bdd"){
                    script {                
                        try {
                            sh "behave -f allure_behave.formatter:AllureFormatter -o allure-results-bug ./features -f pretty --tags=bug -k"
                            ignoreFailures=true

                        } catch(err){
                            echo "Testes com falha"
                                        
                        } finally {
                            // junit allowEmptyResults: true, testResults: 'reports/*.xml'
                            allure ([
                                includeProperties: false,
                                jdk: '',
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: 'allure-results-bug']],
                            ])
                        }                   
                    }
                }               
            }
        }
        stage ('Run Features - FULL') {
            when {
                expression {env.JOB_NAME == "PDGDI_Full_Tests"}
            }
            steps {   
                dir("bdd"){            
                    script {
                    
                        try {
                            sh "behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features -f pretty --tags=full -k"
                            ignoreFailures=true
                        } catch(err){
                            echo "Testes com falha"
                                        
                        } finally {

                            junit allowEmptyResults: true, testResults: 'reports/*.xml'
                            allure ([
                                includeProperties: false,
                                jdk: '',
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: 'allure-results']],  
                            ])   
                        }
                    }
                }
            }   
        }
        stage('Generate Report'){
            steps{
                dir("bdd"){
                    sh "allure-docx ${REPORT_PATH} ${REPORT_NAME}"
                    archiveArtifacts "${REPORT_NAME}"
                }
            }
        }
    }
}