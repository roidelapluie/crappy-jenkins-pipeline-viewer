Crappy Jenkins Pipeline Viewer
----


Usage:

create a settings.py file

    JENKINS_URL="http://jenkins.example.com"
    JENKINS_USER="myuser"
    JENKINS_API_TOKEN="myapikey"

then, in your favourite shell

    make
    ./check-pipeline.py first-job

