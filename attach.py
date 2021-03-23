#!/usr/bin/python
import subprocess
import sys
import os
import pdb

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
        print("Docker not running");
        exit();

def containers():
    process = subprocess.Popen(["docker container ls | sed '1 d' | awk '{ print $NF }'"], stdout=subprocess.PIPE, shell=True)
    conts = process.communicate()[0].decode('utf-8').splitlines()
    return list(set(conts) - set(command_through_cmd))

def shells(my_cont):
    command = "docker exec " + my_cont + " chsh -l"
    process = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()
    if stdout == '':
       return [];

    return list(stdout.decode('utf-8').splitlines())

def keyi(item):
    return int(item) - 1

docker_running()

running_docker_containers = containers()

if len(running_docker_containers) < 1:
    exit("No attachable containers running")

for i, container in enumerate(running_docker_containers):
    print(str(i + 1) + ". " + container)

def in_my_list(ccc):
    try:
        ccc = int(ccc) - 1
        running_docker_containers[ccc]
        return True
    except IndexError:
        return False

while True:
    selected_container = str(get_input("Select Container (press 'q' to exit): "))
    if str(selected_container) == 'q':
        exit();
    if not in_my_list(selected_container):
        continue
    if selected_container.isdigit():
        break

if str(selected_container) == 'q':
    exit();

def clean_and_dedupe(shells):
    cleaned_shell = []
    if shells == None:
        return ""

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
    # pdb.set_trace()
    if not len(shells):
        selected_shell = get_input("Enter the name of your shell (press 'q' to exit): ")
    else:
        selected_shell = get_input("Select Shell (press 'q' to exit or enter the name of a shell): ")

    shell_selected = ""
    if str(selected_shell) == 'q':
        exit();
    elif (selected_shell.isdigit() == True):
        shell_selected = shells[keyi(selected_shell)]
        break
    else:
        shell_selected = selected_shell
        if (shell_selected.isdigit()):
            shell_selected = shells[keyi(selected_shell)]
            break;
        elif (shell_selected in ["bash", "zsh"]):
            break
        else:
            print "Please enter a valid shell ('bash') or press 'q' to exit"

command = 'docker container exec -it ' + container + ' ' + shell_selected

subprocess.call(command, shell=True)
