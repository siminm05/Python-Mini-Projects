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
        if book["available"] == True:
            book["available"] = "Yes"
            print(i, ". ", book["title"], "\nAuthor : ", book["author"], "\nGenre : ", book["genre"], "\nAvailable : ",
                  book["available"], sep="")
            i += 1
            book["available"] = True
        else:
            book["available"] = "No"
            print(i, ". ", book["title"], "\nAuthor : ", book["author"], "\nGenre : ", book["genre"], "\nAvailable : ",
                  book["available"], sep="")
            i += 1
            book["available"] = False



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
            print("Book is now marked borrowed")
            found = True
    if found == False:
        print("No books found with the name:", borrow_name)

def return_book():
    if len(books) == 0:
        print("No Books to return")
        return
    count = 0
    for book in books:
        if book["available"] == False:
            count+=1
    print("Books to be returned:", count)
    if count == 0:
        print("No books need to be returned")
        return
    i = 1
    for book in books:
        if book["available"] == False:
            print(i, ". ", book["title"], sep="")
            i+=1
    found = False
    return_name = input("Enter the name of the book to be returned: ").lower().strip()
    for book in books:
        if book["title"].lower().strip() == return_name:
            book["available"] = True
            print("Book has been marked as returned")
            found = True
            return
    if found == False:
        print("No book was found with the name:", return_name)

def search():
    if len(books) == 0:
        print("No books available for search")
        return
    print("Would you like to search by: ")
    search = False
    i = 1
    search_choice = int(input("1. Title\n2. Author\n3. Genre\nEnter option number:  "))
    if search_choice in [1,2,3]:
        if search_choice == 1:
            title_search = input("Enter title: ").lower().strip()
            for book in books:
                if title_search in book["title"].lower().strip():
                    print(i, ". ", book["title"], "\nAuthor : ", book["author"], "\nGenre : ", book["genre"],
                          "\nAvailable : ", book["available"], sep="")
                    i += 1
                    search = True
        elif search_choice == 2:
            author_search = input("Enter name of the author: ").lower().strip()
            for book in books:
                if author_search in book["author"].lower().strip():
                    print(i, ". ", book["title"], "\nAuthor : ", book["author"], "\nGenre : ", book["genre"],
                          "\nAvailable : ", book["available"], sep="")
                    i += 1
                    search = True
        else:
            genre_search = input("Enter genre: ").lower().strip()
            for book in books:
                if genre_search in book["genre"].lower().strip():
                    print(i, ". ", book["title"], "\nAuthor : ", book["author"], "\nGenre : ", book["genre"],
                          "\nAvailable : ", book["available"], sep="")
                    i += 1
                    search = True
        if search == False:
            print("No book/s found")
    else:
        print("Please enter number [1-3]")
def main():
    while True:
        try:
            print("\n---Library Management System---")
            print("1. Add\n2. View\n3. Borrow\n4. Return\n5. Search\n6. Exit\n")
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add()
            elif user_choice == 2:
                view()
            elif user_choice == 3:
                borrow()
            elif user_choice == 4:
                return_book()
            elif user_choice == 5:
                search()
            elif user_choice == 6:
                print("Thank you for using Library Management System")
                break
            else:
                print("Enter a number from the menu")

        except ValueError:
            print("Invalid input type. Enter number")

main()
