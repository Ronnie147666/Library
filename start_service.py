import subprocess
import os

commands = [
 ##   'sudo -s',
    'docker rm -f $(docker ps -a -q)',
    'docker-compose -f docker-compose-kafka-spark.yml up', 
    'docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:latest'
    ]
## run in parallel
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]


