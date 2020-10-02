import subprocess
import os

commands = [
    'cd ~/147/TBU-Ecosystem/BattleGenerator && docker build -t nick147/generator .',
    'cd ~/147/TBU-Ecosystem/CloudBase && docker build -t nick147/config .',
    'cd ~/147/TBU-Ecosystem/Datahouse && docker build -t nick147/data .',
    'cd ~/147/TBU-Ecosystem/Eureka && docker build -t nick147/eureka .',
    'cd ~/147/TBU-Ecosystem/TBU && docker build -t nick147/tbu .'
    ]
## run in parallel
processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]


