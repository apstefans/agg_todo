#!/usr/bin/env python3
# An Aggresive ToDo list
# The rudest ToDo list you'll ever see


# The list of tasks
tasks = []

# ANSI Colors
GREEN = "\33[1;32m"
GREENBLINK = GREEN + "\33[5;32m"
MAGENTA = "\33[1;35m"
YELLOW = "\33[1;33m"
YELLOWBLINK = YELLOW + "\33[5;33m"
RED = "\33[1;31m"
REDBLINK = RED + "\33[5;31m"
BLUE = "\33[1;34m"
TERMCOLOR = "\33[0m"

# Main menu
def start():
    print(" ")
    print(MAGENTA + "** The " + RED + "AGGRESIVE " + TERMCOLOR + MAGENTA + "To-Do list! **" + TERMCOLOR)
    print(" ")
    print(MAGENTA + "1. Add a task " + TERMCOLOR + "    | Not like you'll do it")
    print(RED + "2. Delete a task " + TERMCOLOR + " | Because you never follow through")
    print(BLUE + "3. View tasks " + TERMCOLOR + "    | So you can see the things you'll never accomplish")
    print(YELLOW + "q. Quit program " + TERMCOLOR + "  | Because your mother raised a quitter")
    print(" ")
    choice = input(RED + "Select an option if you can be arsed to: ")
    print(" ")
    if choice == "1":
        add_task()
        print(" ")
    elif choice == "2":
        del_task()
        print(" ")
    elif choice == "3":
        view_tasks()
        print(" ")
    elif choice == "q":
        quit()
    else:
        print(GREEN + "Do you not know how to use a keyboard? The options are clearly listed" + TERMCOLOR)

# Add a task
def add_task():
    new_task = input(MAGENTA + "What do you think you'll accomplish? " + TERMCOLOR)
    print(" ")
    tasks.append(new_task)
    print("\n" * 100)
    print(GREEN + "I've added", REDBLINK + new_task, TERMCOLOR + GREEN + "to your list.")
    print("Let's see if you'll actually do it you lazy cunt." + TERMCOLOR)

# Delete a task
def del_task():
    if  len(tasks) == 0:
        print("\n" * 100)
        print(GREEN + "You first need to decide to actually do something before you decide not to. Stupid." + TERMCOLOR)
    else:
        print(MAGENTA + "These are your current tasks: " + TERMCOLOR)
        for i, task in enumerate(tasks):
            print(i + 1, BLUE + task + TERMCOLOR)
        print(" ")
        TERMCOLOR
        try:
            choice = int(input(MAGENTA + "Which task have you given up on? (0 to cancel) " + TERMCOLOR))
            print(" ")
            if choice > 0 and choice <= len(tasks):
                del tasks[choice-1]
                print("\n" * 100)
                print(GREEN + "You give up too easily.")
                print("Don't try and convince me that you actually")
                print("completed that task.")
                print(" ")
                if len(tasks) > 0:
                    print(MAGENTA +"You'll still have to finish these tasks though: " + TERMCOLOR)
                else:
                    print(MAGENTA + "Looks like your task list is empty. You really are lazy.")
                for i, task in enumerate(tasks):
                    print(i + 1, BLUE + task + TERMCOLOR)                        
            elif choice == 0:
                print("\n" * 100)
                print(GREEN + "Indecisive are we?")
            else:
                print("\n" * 100)
                print(GREEN + "For fuck sake, pick a task that's there. Try again and don't fail this time!" + TERMCOLOR)
                print(" ")
                del_task()
        except:
            print("\n" * 100)
            print(YELLOWBLINK + YELLOW + "THAT'S NOT EVEN A NUMBER! WHAT ARE YOU?! " + TERMCOLOR)
            print(GREEN + "Try again, and since you need a reminder, here is a list of numbers:")
            print(MAGENTA + "0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9")
            print(GREEN + "Anything else is" + REDBLINK + RED, "NOT" + TERMCOLOR + GREEN,"a number." + TERMCOLOR)
            print(" ")
            del_task()

# View the task list
def view_tasks():
    if len(tasks) == 0:
        print("\n" * 100)
        print(GREEN + "You don't have any tasks. I knew you were no good." + TERMCOLOR)
        #print(" ")
    else:
        print("\n" * 100)
        print(MAGENTA + "These are the tasks you've not done yet:" + TERMCOLOR)
        print(" ")

        for i, task in enumerate(tasks):
            print(i + 1, BLUE + task + TERMCOLOR)

# Quit program
def quit():
    print("\n" * 100)
    print(GREEN + "Fine. Go then. I didn't like you anyway.")
    print(GREENBLINK + "." + REDBLINK + "." + YELLOWBLINK + "." + BLUE + "." + MAGENTA + "." + GREENBLINK + "." + REDBLINK + "." + YELLOWBLINK + "." + BLUE + "." + MAGENTA + "." + GREENBLINK + "." + REDBLINK + "." + YELLOWBLINK + "." + BLUE + "." + MAGENTA + "." + GREENBLINK + "." + REDBLINK + "." + YELLOWBLINK + "." + BLUE + "." + MAGENTA + "." + GREENBLINK + "." + TERMCOLOR)
    print(YELLOWBLINK + "          .-.\n          |" + BLUE + "U" + YELLOWBLINK + "|\n          | |\n          | |\n         _| |_\n        | | | |-. \n       /|     ` |\n      | |       |\n      |         |\n      \         /\n       |       |\n       |       |\n" + TERMCOLOR)    
    print(MAGENTA + "          Cunt." + TERMCOLOR)
    exit()

print("\n" * 100)
def main():
    while True:
        start()

if __name__ == "__main__":
    main()


    
 