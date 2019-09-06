import subprocess
import os

commands = [
    'docker rm -f $(docker ps -a -q)',
    'cd DockerKafka && docker-compose up -d', 
    'cd DockerSpark && docker-compose up -d',
    'docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:latest'
    ]
## run in parallel
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]


