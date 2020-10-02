import subprocess
import os

commands = [
    'cd ~/147/TBU-Ecosystem/DomainCentral && mvn clean install -DskipTests',
    'cd ~/147/TBU-Ecosystem/BattleGenerator && mvn clean install -DskipTests',
    'cd ~/147/TBU-Ecosystem/CloudBase && mvn clean install -DskipTests',
    'cd ~/147/TBU-Ecosystem/Datahouse && mvn clean install -DskipTests',
    'cd ~/147/TBU-Ecosystem/Eureka && mvn clean install -DskipTests',
    'cd ~/147/TBU-Ecosystem/TBU && mvn clean install -DskipTests'
 ##   'cd ~/147/ZuulGatekeeper && mvn clean install -DskipTests'
    ]
## run in parallel
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]


