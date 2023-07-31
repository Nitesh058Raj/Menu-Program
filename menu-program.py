import os

from option_functions import *

isOn = True
title = "Welcome to the Menu Program!"
menu = []


def setup():
    global isOn
    isOn = True
    global title
    title = "Welcome to the Menu Program!"
    global menu
    menu = [
        "1. View Docker Info",
        "2. List Docker Containers",
        "3. Run Ansible Playbook",
        "4. View Disk Space",
        "5. List Files in Directory",
        "6. Tell Me a Fortune",
        "7. Display a Funny Cow",
        "10. Exit"
    ]


def clearScreen():
    os.system("clear")


def printTitle(text):

    print("+" + 32 * "-" + "+")
    print("|" + 32 * " " + "|")
    print("|" + ((33 - len(text)) // 2) * " " +
          text + ((33 - len(text)) // 2) * " " + "|")
    print("|" + 32 * " " + "|")
    print("+" + 32 * "-" + "+")


def printMenu():
    global title
    global menu

    clearScreen()
    printTitle(title)
    for i in menu:
        print(i)


def menuChoice():
    global isOn

    choice = input("Enter your choice: ")
    if choice == "1":
        view_docker_info()
    elif choice == "2":
        list_docker_containers()
    elif choice == "3":
        run_ansible_playbook()
    elif choice == "4":
        view_disk_space()
    elif choice == "5":
        list_files_in_directory()
    elif choice == "6":
        tell_me_fortune()
    elif choice == "7":
        display_funny_cow()
    elif choice == "10" or choice.lower() in ["q", "quit", "exit"]:
        print("Exiting...")
        isOn = False
    else:
        print("Invalid choice")


def main():
    global isOn
    setup()

    try:
        while isOn:
            printMenu()
            menuChoice()
            input("Press enter to continue...")
            clearScreen()
    except KeyboardInterrupt:
        print("Exiting...")
        isOn = False


main()
