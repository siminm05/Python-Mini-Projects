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
            print(1, ". ", contact["name"], " - ", contact["phoneNum"], sep="")
            i+=1

def main():
    while True:
        try:
            print("\n1. Add\n2. View\n3. Exit")
            user_choice = int(input("Enter your choice: "))
            if user_choice==1:
                add()
            elif user_choice==2:
                view()
            elif user_choice==3:
                print("Thank you")
                break
        except ValueError:
            print("Invalid input type. Enter a number")

main()
