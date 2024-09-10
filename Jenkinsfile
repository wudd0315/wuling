pipeline{
    agent any
    parameters {
        string(name:'caseDir', defaultValue:'online_device_inspection', description:'用例目录')
        string(name:'mark', defaultValue:'memory', description: '用例标记，支持pytest.mark 表达式')
        }
    stages{
        stage('拉取代码') {
            steps {
                git branch: 'master', credentialsId: '2eaff256-2a8a-4126-9264-f0790f5e99b9', url: 'https://github.com/wudd0315/wuling.git'
            }
        }
        stage("安装依赖"){
            steps {
                script {
                sh 'pip install -r requirements.txt'
                }
            }
        }
        stage("执行测试"){
            steps {
                script{
                sh 'pytest'
                }
            }
        }
    }
    post{
        always{
            echo 'always say goodbay'
        }
    }
}
