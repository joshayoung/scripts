#!/usr/bin/python
import subprocess
import sys

def get_input(inp):
    if sys.version_info < (3, 0):
        return raw_input(inp)
    else:
        return input(inp)

def docker_running():
    try:
        subprocess.check_output("docker stats --no-stream", stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError:
        print "Docker not running"
        exit()

def containers():
    process = subprocess.Popen(["docker container ls | sed '1 d' | awk '{ print $NF }'"], stdout=subprocess.PIPE, shell=True)
    return process.communicate()[0].decode('utf-8').splitlines()

def keyi(item):
    return int(item) - 1

docker_running()

running_docker_containers = containers()
shells = ['sh', 'bash', 'zsh']

if len(running_docker_containers) < 1:
    exit("No containers running")

for i, container in enumerate(running_docker_containers):
    print(str(i + 1) + ". " + container)

selected_container = str(get_input("Select Container (press 'q' to exit): "))

if str(selected_container) == 'q':
    exit();

for i, shell in enumerate(shells):
    print(str(i + 1) + ". " + shell);

selected_shell = get_input("Select Shell (press 'q' to exit): ")

if str(selected_shell) == 'q':
    exit();

container = running_docker_containers[keyi(selected_container)]
command = 'docker container exec -it ' + container + ' ' + shells[keyi(selected_shell)]

subprocess.call(command, shell=True)
