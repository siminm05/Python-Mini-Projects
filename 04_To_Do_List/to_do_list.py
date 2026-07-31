tasks = []

while True:
        try:
            print("1. Add Task\n2. View Tasks\n3. Exit")
            user_choice = int(input("Choose an option [1 to 3]: "))

            if user_choice == 1:
                user_task = input("Enter Task: ")
                tasks.append(user_task)
                continue
            elif user_choice == 2:
                i = 1
                if len(tasks) == 0:
                    print("No tasks to do")
                else:
                    print("Current Tasks: ")
                    for task in tasks:
                        print(i,". ",task,sep="")
                        i+=1
                    print("")
                continue
            elif user_choice == 3:
                print("Thank you")
                break
            else:
                print("Enter number [1 to 3]")

        except ValueError:
            print("Invalid value type. Enter number [1 to 3]")

