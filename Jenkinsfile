node {
    stage('Build') {
                echo "checkout from SCM"
                echo "========== init =========="
                sh "rm -rf *"
                git 'https://github.com/dplinjy/simple-script.git'
                // Make the output directory.

                sh "mkdir output"
                sh "ls -l"
                writeFile file: "output/test_log.txt", text: ""
                echo "Archive build output"

                // Archive the build output artifacts.
                archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
    }
    stage('Test') {

        echo "========== run py =========="
        sh "python -m unittest -v testCalculate.py"
        sh "ls -l"
        echo "========== analyse result =========="
        sh "cat ./TestResult.txt >output/test_log.txt"
        sh "ls -l"
        archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
        //String readString = readFile("output/test_log.txt")
        //echo "test print readFile"
        //echo readString
        //Boolean buildResult = readString.matches("(.*)FAIL(.*)")

        //try {
        //    assert buildResult == false
        //} catch (AssertionError e) {
        //    echo "exception found......"
        //    throw e
        //}

    }
    stage('Deploy') {
       sh "cat output/test_log.txt"
       sh "pwd"
    }
}
