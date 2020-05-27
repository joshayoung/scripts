#!/usr/bin/python
import subprocess

def containers():
    process = subprocess.Popen(["docker ps | sed '1 d' | awk '{ print $NF }'"], stdout=subprocess.PIPE, shell=True)
    return process.communicate()[0].decode('utf-8').splitlines()

def key(item):
    return int(item - 1)

running_docker_containers = containers()
shells = ['sh', 'bash', 'zsh']

for i, container in enumerate(running_docker_containers):
    print(str(i + 1) + ". " + container)

selected_container = input("Select Container: ")

for i, shell in enumerate(shells):
    print(str(i + 1) + ". " + shell);

selected_shell = input("Select Shell: ")

container = running_docker_containers[key(selected_container)]
command = 'docker exec -it ' + container + ' ' + shells[key(selected_shell)]

subprocess.call(command, shell=True)
