books = []

#'''
books.append({"genre": "Self Help",
            "title": "Atomic Habits",
            "author": "James Clear",
            "available": True})
books.append({"genre": "Fantasy",
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "available": True})
#'''
def add():
    genre = input("Enter genre: ")
    title = input("Enter title: ")
    author = input("Enter name of the author: ")
    books.append({"genre": genre,
                  "title": title,
                  "author": author,
                  "available": True})
    print("Book has been added into the system")

def view():
    if len(books) == 0:
        print("No books to view")
        return
    i = 1
    for book in books:
        print(i, ". ", book["title"],"\nAuthor : ", book["author"], "\nGenre : ", book["genre"], "\nAvail : ", book["available"],sep="")
        i += 1


def borrow():
    if len(books) == 0:
        print("No books available to borrow")
        return
    count=0
    for book in books:
        if book["available"]:
            count+=1
    print("Books available to borrow:", count)
    if count == 0:
        print("We are sorry. All books are currently borrowed")
        return
    i = 1
    for book in books:
        if book["available"]:
            print(i, ". ", book["title"], sep="")
            i += 1
    borrow_name = input("Enter the name of the book you would like to borrow: ").lower().strip()
    found = False
    for book in books:
        if book["title"].lower().strip() == borrow_name:
            book["available"] = False
            print("Book is now yours")
            found = True
    if found == False:
        print("No books found with the name:", borrow_name)

def main():
    while True:
        try:
            print("\n---Library Management System---")
            print("1. Add\n2. View\n3. Borrow\n4. Exit\n")
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add()
            elif user_choice == 2:
                view()
            elif user_choice == 3:
                borrow()
            elif user_choice == 4:
                print("Thank you for using Library Management System")
                break
            else:
                print("Enter a number from the menu")

        except ValueError:
            print("Invalid input type. Enter number")

main()
