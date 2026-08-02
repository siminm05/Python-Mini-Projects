tasks = []

def menu(user_choice):
    while True:
        if user_choice == 1:
            user_task = input("Enter Task: ")
            if user_task.strip() != "":
                tasks.append({
                    "task": user_task,
                    "completed": False})
                break
            else:
                print("Task cant be empty")
                continue

        if len(tasks) == 0:
            print("No tasks available. Add new task.")
        else:
            if user_choice == 2:
                view_tasks()
                return
            elif user_choice == 3:
                delete_task()
                return
            elif user_choice == 4:
                complete_task()
                return
            elif user_choice == 5:
                edit_task()
                return
            else:
                print("Enter number")

def view_tasks():
    i = 1
    for task in tasks:
        if task["completed"]:
            print(i, ". ✓ ", task["task"], sep="")
        else:
            print(i, ". ✗ ", task["task"], sep="")
        i += 1


def delete_task():
    while True:
        try:
            view_tasks()
            print("\nWhich task would you like to delete? ")
            delete_index = int(input("Enter the index next to the task: "))
            if 0 < delete_index <= len(tasks):
                print("Task '", tasks[delete_index - 1]["task"], "' has been deleted", sep="")
                tasks.pop(delete_index - 1)
                return
            else:
                print("Invalid Task number\n")
        except ValueError:
            print("\nInvalid Input type. Enter task index\n")

def complete_task():
    while True:
        try:
            view_tasks()
            print("\nWhich task would to like to mark 'Completed'?")
            complete_index = int(input("Enter the index next to the task: "))
            if 0 < complete_index <= len(tasks):
                # if tasks[complete_index - 1]["completed"] == False:
                if not tasks[complete_index - 1]["completed"]:
                    print("Task '", tasks[complete_index-1]["task"], "' has been marked completed", sep="")
                    tasks[complete_index-1]["completed"] = True
                    return
                else:
                    print("Task has already been completed")
            else:
                print("Invalid Task Number\n")
        except ValueError:
            print("\nInvalid input type. Enter task index\n")

def edit_task():
    while True:
        try:
            print("\nWhich task would you like to 'edit'?")
            view_tasks()
            edit_index = int(input("Enter the index next to the task: "))
            if 0 < edit_index <= len(tasks):
                new_user_task = input("Enter the task: ")
                if new_user_task.strip() != "":
                    print("Task '", tasks[edit_index - 1]["task"], "' has been edited\n", sep="")
                    tasks[edit_index-1]["task"] = new_user_task
                    break
                else:
                    print("Task cant be empty.")
            else:
                print("Enter index number")
        except ValueError:
            print("Invalid input type. Enter number")
def main():
    while True:
        try:
            print("\n1. Add\n2. View\n3. Delete\n4. Mark Complete\n5. Edit\n6. Exit")
            user_choice = int(input("Choose an option: "))
            print("")
            if user_choice == 6:
                print("Thank you")
                break
            else:
                menu(user_choice)

        except ValueError:
            print("Invalid value type. Enter number")

main()
