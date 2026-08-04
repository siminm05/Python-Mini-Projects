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
        print(i, ". ", book["title"],"\nAuthor : ", book["author"], "\nGenre : ", book["genre"], "\n",sep="")
        i += 1

def main():
    while True:
        try:
            print("\n---Library Management System---")
            print("1. Add\n2. View\n3. Exit\n")
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add()
            elif user_choice == 2:
                view()
            elif user_choice == 3:
                print("Thank you for using Library Management System")
                break
            else:
                print("Enter a number from the menu")

        except ValueError:
            print("Invalid input type. Enter number")

main()
