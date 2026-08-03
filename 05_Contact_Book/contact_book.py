contact_book =[]

def add():
    name = input("\nEnter Name: ")
    phone_num = input("Enter Phone Number: ")
    if len(phone_num) == 10:
        contact_book.append({"name": name,
                         "phone_num": phone_num})
    else:
        print("Invalid Number of digits")
        return
    print("Contact have been added")
def view():
    i=1
    if len(contact_book) == 0:
        print("No contacts to view. Add contact")
    else:
        for contact in contact_book:
            print(i, ". ", contact["name"], " - ", contact["phone_num"], sep="")
            i+=1

def delete():
    try: 
        if len(contact_book)==0:
            print("No contacts to delete. Add contact")
            return
        else:
            view()
            print("\nWhich contact would you like to delete?")
            delete_index = int(input("Enter the index next to the contact: "))
            if 0 < delete_index <= len(contact_book):
                contact_book.pop(delete_index-1)
            else:
                print("Please Enter the correct index number")
                return
            print("Contact has been deleted")
    except ValueError:
        print("Invalid Input type")


def main():
    while True:
        try:
            print("\n1. Add\n2. View\n3. Delete\n4. Exit")
            user_choice = int(input("Enter your choice: "))
            if user_choice==1:
                add()
            elif user_choice==2:
                view()
            elif user_choice==3:
                delete()
            elif user_choice==4:
                print("Thank you")
                break
            else:
                print("Enter a number from the menu")
        except ValueError:
            print("Invalid input type. Enter a number")



main()
