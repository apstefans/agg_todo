# An Aggresive ToDo list

# The list of tasks
tasks = []

# Add a task
def add_task():
    new_task = input("What do you think you'll accomplish? ")
    print(" ")
    tasks.append(new_task)
    print("I've added", new_task, "to your list.")
    print("Let's see if you'll actually do it you lazy cunt.")
    print(" ")

# Delete a task
def del_task():
    if  len(tasks) == 0:
        print("You first need to decide to actually do something before you decide not to. Stupid.")
        print(" ")
    else:
        print("These are your current tasks: ")
        for i, task in enumerate(tasks):
            print(i + 1, task)
        print(" ")
        choice = int(input("Which task have you given up on? "))
        print(" ")
        if choice > 0 and choice <= len(tasks):
            del tasks[choice-1]
            print("You give up too easily.")
            print("Don't try and convince me that you actually")
            print("completed that task.")
            print(" ")
            print("You'll still have to finish these tasks though: ")
            for i, task in enumerate(tasks):
                print(i + 1, task)
            print(" ")
        else:
            print("For fuck sake, pick a task that's there. Try again and don't fail this time!")
            print(" ")
            del_task()
            print(" ")


# View the task list
def view_tasks():
    if len(tasks) == 0:
        print("You don't have any tasks. I knew you were no good")
        print(" ")
    else:
        print("These are the tasks you've not done yet")
        print(" ")
        for i, task in enumerate(tasks):
            print(i + 1, task)
    print(" ")
    

def main():
    while True:
        print("** The Aggresive To-Do list! **")
        print("1. Add a task... not like you'll do it")
        print("2. Delete a task. Because you never follow through.")
        print("3. View tasks. So you can see the things you'll never accomplish")
        print("q. Quit program. Because your mother raised a quitter.")
        print(" ")

        choice = input("Select an option if you can be arsed to: ")
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
            print("Fine. Go then. I didn't like you anyway. Cunt.")
            break
        else:
            print("Do you not know how to use a keyboard? The options are clearly listed")
            print(" ")

if __name__ == "__main__":
    main()