isOn = True
title = "Welcome to the Menu Program!"
menu = []

def setup():
    global isOn 
    isOn = True
    global title 
    title = "Welcome to the Menu Program!"
    global menu 
    menu = ["1. Option 1", "2. Option 2", "3. Option 3", "4. Exit"]

def clearScreen():
    print("\033c", end="")

def printTitle():
    global title

    print("+" + 32 * "-" + "+")
    print("|" + 32 * " " + "|")
    print("|" + ((33 - len(title)) // 2) * " " + title + ((33 - len(title)) // 2) * " " + "|")
    print("|" + 32 * " " + "|")
    print("+" + 32 * "-" + "+")

def printMenu():
    global title
    global menu

    clearScreen()
    printTitle()
    for i in menu:
        print(i)

def menuChoice():
    global isOn
 
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You chose option 1")
    elif choice == "2":
        print("You chose option 2")
    elif choice == "3":
        print("You chose option 3")
    elif choice == "4" or "q" or "Q":
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
