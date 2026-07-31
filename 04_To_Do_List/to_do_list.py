tasks = []


def view_tasks():
    i = 1
    print("Current Tasks: ")
    for task in tasks:
        print(i, ". ", task, sep="")
        i += 1


def delete_task():
    while True:
        try:
            view_tasks()
            print("\nWhich task would you like to delete? ")
            delete_index = int(input("Enter the index next to the task: "))
            if 0 < delete_index <= len(tasks):
                print("Task '", tasks[delete_index - 1], "' has been deleted", sep="")
                tasks.pop(delete_index - 1)
            else:
                print("Invalid Task number\n")
        except ValueError:
            print("\nInvalid Input type. Enter task index\n")

while True:
    try:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        user_choice = int(input("Choose an option [1 to 4]: "))
        print("")

        if user_choice == 1:
            user_task = input("Enter Task: ")
            tasks.append(user_task)
            continue

        elif user_choice == 2:
            if len(tasks) == 0:
                print("No tasks to do")
            else:
                view_tasks()
            continue

        elif user_choice == 3:
            if len(tasks) == 0:
                print("No tasks to be deleted")
            else:
                delete_task()
            continue

        elif user_choice == 4:
            print("Thank you")
            break

        else:
            print("Enter number [1 to 4]")

    except ValueError:
        print("Invalid value type. Enter number [1 to 4]")
