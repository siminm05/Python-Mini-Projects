import string

contact_book =[]

def add():
    name = input("\nEnter Name: ")
    phone_num = input("Enter Phone Number: ")
    if len(phone_num) == 10:
        if phone_num.isdigit():
            contact_book.append({"name": name,
                            "phone_num": phone_num})
        else:
            print("Please enter number [0-9]")
            return
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

def edit():
    try:
        if len(contact_book) == 0:
            print("No contact to edit")
        else:
            print("\nWhat would you like to edit? \n1. Name\n2. Phone Number")
            edit_choice = int(input("Enter 1 or 2: "))
            if edit_choice in [1,2]:
                view()
                print("Which contact would you like to edit?")
                edit_index = int(input("Enter the index number next to the contact: "))
                if 0 < edit_index <= len(contact_book):
                    if edit_choice == 1:
                        new_name = input("Enter new name: ")
                        contact_book[edit_index-1]["name"] = new_name
                        print("Name has been changed")
                    else:
                        new_number = input("Enter new number: ")
                        if len(new_number) == 10:
                            contact_book[edit_index-1]["phone_num"] = new_number
                            print("Phone Number has been changed")
                        else:
                            print("Phone Number should be of 10 digits only")
                else:
                    print("Wrong index number")
            else:
                print("Please select number 1 or 2")
    except ValueError:
        print("Invalid Input type")


def search():
    if len(contact_book)==0:
        print("No contact to find")
    else:
        found = False
        search = input("Enter name (Exact match not require): ").lower().strip()
        print("Found: ")
        for contact in contact_book:
            if search in contact["name"].lower():
                print(contact["name"], " - ", contact["phone_num"])
                found = True
        if not found:
            print("No contact")


def main():
    while True:
        try:
            print("\n1. Add\n2. View\n3. Delete\n4. Edit\n5. Search\n6. Exit")
            user_choice = int(input("Enter your choice: "))
            if user_choice==1:
                add()
            elif user_choice==2:
                view()
            elif user_choice==3:
                delete()
            elif user_choice==4:
                edit()
            elif user_choice == 5:
                search()
            elif user_choice==6:
                print("Thank you")
                break
            else:
                print("Enter a number from the menu")
        except ValueError:
            print("Invalid input type. Enter a number")



main()
