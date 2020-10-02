import subprocess
import os

commands = [
    'cd ~/147/TBU-Ecosystem/BattleGenerator && docker push nick147/generator:latest',
    'cd ~/147/TBU-Ecosystem/CloudBase && docker push nick147/config:latest',
    'cd ~/147/TBU-Ecosystem/Datahouse && docker push nick147/data:latest',
    'cd ~/147/TBU-Ecosystem/Eureka && docker push nick147/eureka:latest',
    'cd ~/147/TBU-Ecosystem/TBU && docker push nick147/tbu:latest'
    ]
## run in parallel
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]


