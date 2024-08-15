pipeline{
    agent any
    parameters {
        string(name:'caseDir', defaultValue:'online_device_inspection', description:'用例目录')
        string(name:'mark', defaultValue:'memory', description: '用例标记，支持pytest.mark 表达式')
        }
    tools {
    allure('allure') //使用allure工具
    }
    stages{
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
