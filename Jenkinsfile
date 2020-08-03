node {
    stage('Build') {
                echo "checkout from SCM"
                sh "rm -rf *"
                git 'https://github.com/dplinjy/simple-script.git'
                // Make the output directory.
                sh "ls -l"
                echo "debug"

                //sh "mkdir -p output"
                sh "mkdir output"
                //sh "ls -r"
                sh "ls -r"
                // Write an useful file, which is needed to be archived.
                //writeFile file: "output/usefulfile.txt", text: "This file is useful, need to archive it."
                writeFile file: "output/test_log.txt", text: ""
                // Write an useless file, which is not needed to be archived.
                //writeFile file: "output/uselessfile.md", text: "This file is useless, no need to archive it."

                echo "Archive build output"

                // Archive the build output artifacts.
                archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
    }
    stage('Test') {
      // sh " echo https://github.com/lzjun567/python_scripts |  /usr/bin/python   02_find_all_links.py >testlog.log"

        echo "run py......"
        //timeout(6) {
        //    waitUntil {
        //        sh "python -m unittest -v testCalculate.py"
        //    }
        //}
        sh "python -m unittest -v testCalculate.py"
        sh "ls -l"
        echo "analyse result......"
        sh "cat ./TestResult.txt > ./output/test_log.txt"
        sh "ls -l"
        //def result = readFile("TestResult.txt")
        //result = readFile("TestResult.txt")
        //sh "${result}"
        //sh "TestResult=$(cat TestResult.txt)"
        //echo "${TestResult}"
        //sh "diff testlog.txt reflog.txt"
        //sh "diff testlog.txt reflog.txt >diff.txt"
        //sh "cp diff.txt diff.sh"
          // Archive the build output artifacts.
        //archiveArtifacts artifacts: '*.sh', excludes: '*.md'
        //archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
        //sh "cat diff.txt"
        readString = readFile("output/test_log.txt")
        echo "test print readFile"
        echo ${readString}

    }
    stage('Deploy') {
       sh "cat output/test_log.txt"
    }
}
