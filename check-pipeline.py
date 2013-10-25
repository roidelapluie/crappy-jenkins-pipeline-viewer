#!bin/python

import jenkins
from termcolor import colored
import re
import sys
from time import sleep

try:
    from settings import JENKINS_URL, JENKINS_USER, JENKINS_API_TOKEN
except ImportError:
    print """

You need to add a setting.py file wich contains:

JENKINS_URL="http://jenkins.example.com"
JENKINS_USER="myuser"
JENKINS_API_TOKEN="myapikey"
        """


j = jenkins.Jenkins(JENKINS_URL, JENKINS_USER, JENKINS_API_TOKEN)


print("\033[H\033[2J")
def show_job(job):
    job = j.get_job_info(job)
    color = job['color']
    attr = None
    on_color = None
    if re.search('.*_.*', color):
        colors = color.split('_')
        color = colors[0]
        attr = ["blink"]
    if color == 'disabled':
        color = 'white'
        on_color = 'on_grey'
    if color == 'blue':
        color = 'green'
    print "\033[K" + colored(job['name'], color, on_color, attr),
    if len(job['builds']) > 0:
        build_number = job['builds'][0]['number']
        print colored('#'+str(build_number), 'grey', 'on_white'),
    try:
        changes = j.get_build_info(job['name'],build_number)['changeSet']['items']
        change = changes[0]
        print change['author']['fullName'],
        print change['commitId'][:8],
        if len(changes) > 1:
            print '+',len(changes) -1,
    except:
        pass
    print ""
    if job.has_key('downstreamProjects') and len(job['downstreamProjects']) > 0:
        show_job(job['downstreamProjects'][0]['name'])

while True:
    print("\033[0;0H")
    show_job(sys.argv[1])
    sleep(5)
