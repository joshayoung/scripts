#!/usr/bin/python
import subprocess
import sys
import os

command_through_cmd = []
try: 
    command_through_cmd = sys.argv[1].split(',')
except IndexError:
    ""

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
    containers = process.communicate()[0].decode('utf-8').splitlines()
    return list(set(containers) - set(command_through_cmd))

def shells(cont):
    command = "docker exec " + cont + " chsh -l"
    process = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    shells = process.communicate()[0].decode('utf-8').splitlines()
    return list(shells)

def keyi(item):
    return int(item) - 1

docker_running()

running_docker_containers = containers()

if len(running_docker_containers) < 1:
    exit("No attachable containers running")

for i, container in enumerate(running_docker_containers):
    print(str(i + 1) + ". " + container)

while True:
    selected_container = str(get_input("Select Container (press 'q' to exit): "))
    if str(selected_container) == 'q':
        exit();
    if selected_container.isdigit() == True:
        break

if str(selected_container) == 'q':
    exit();

def clean_and_dedupe(shells):
    cleaned_shell = []
    for i, shell in enumerate(shells):
        base = os.path.basename(shell)
        if base in cleaned_shell:
            continue
        cleaned_shell.append(base)
    return cleaned_shell

container = running_docker_containers[keyi(selected_container)]
shells = clean_and_dedupe(shells(container))

for i, shell in enumerate(shells):
    print(str(i + 1) + ". " + shell);

while True:
    selected_shell = get_input("Select Shell (press 'q' to exit): ")
    if str(selected_shell) == 'q':
        exit();
    if selected_shell.isdigit() == True:
        break

command = 'docker container exec -it ' + container + ' ' + shells[keyi(selected_shell)]

subprocess.call(command, shell=True)
