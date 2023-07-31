import os


def view_docker_info():
    os.system("docker info")


def list_docker_containers():
    os.system("docker ps -a")


def run_ansible_playbook():
    playbook = input("Enter playbook name: ")
    os.system("ansible-playbook" + playbook)


def view_disk_space():
    os.system("df -h")


def list_files_in_directory():
    os.system("ls -l")


def tell_me_fortune():
    os.system("fortune")


def display_funny_cow():
    text = input("Enter text: ")
    os.system("cowsay " + text)
