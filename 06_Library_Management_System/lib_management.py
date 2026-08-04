books = []


# '''
def add_books():
    books.append({"genre": "Self Help",
                  "title": "Atomic Habits",
                  "author": "James Clear",
                  "available": True})
    books.append({"genre": "Fantasy",
                  "title": "Harry Potter",
                  "author": "J.K. Rowling",
                  "available": True})
    books.append({"genre": "Fantasy",
                  "title": "A Game of Thrones",
                  "author": "George R.R. Martin",
                  "available": False})
    books.append({"genre": "Business",
                  "title": "The Total Money Makeover",
                  "author": "Dave Ramsey",
                  "available": True})
    books.append({"genre": "Science Fiction",
                  "title": "Dune",
                  "author": "Frank Herbert",
                  "available": False})
    books.append({"genre": "Mystery",
                  "title": "Gone Girl",
                  "author": "Gillian Flynn",
                  "available": True})
    books.append({"genre": "Mystery",
                  "title": "The Silent Patient",
                  "author": "Alen Michaelides",
                  "available": True})


# '''
def add():
    while True:
        genre = input("Enter genre: ")
        if genre.strip() == "":
            print("Genre cant be empty")
            continue
        break
    while True:
        title = input("Enter title: ")
        if title.strip() == "":
            print("Title of the book cant be empty")
            continue
        break
    while True:
        author = input("Enter name of the author: ")
        if author.strip() == "":
            print("Author name cant be empty")
            continue
        break
    books.append({"genre": genre,
                  "title": title,
                  "author": author,
                  "available": True})
    print("Book has been added into the system")
    return


def view():
    if len(books) == 0:
        print("No books to view")
        return
    i = 1
    for book in books:
        book_info = print_book(book)
        print(i, book_info, sep="")
        i += 1


def print_book(book):
    book_info = ""
    if book["available"]:
        #book_info = ". " + book["title"] + "\nAuthor : " + book["author"] + "\nGenre : " + book["genre"] + "\nAvailable : Yes"
        book_info = ". " + book["title"] + " - " + book["author"] +" - "+ book["genre"] +" - Yes"
    else:
        book_info = ". " + book["title"] + " - " + book["author"] +" - "+ book["genre"] +" - No"
    return book_info


def borrow():
    if len(books) == 0:
        print("No books available to borrow")
        return
    count = 0
    for book in books:
        if book["available"]:
            count += 1
    print("Books available to borrow:", count)
    if count == 0:
        print("All books are currently borrowed")
        return
    i = 1
    for book in books:
        if book["available"]:
            print(i, ". ", book["title"], sep="")
            i += 1
    while True:
        borrow_name = input("Enter the name of the book you would like to borrow: ").lower().strip()
        found = False
        if borrow_name.strip() == "":
            print("Name cant be empty")
            continue
        break
    for book in books:
        if book["title"].lower().strip() == borrow_name:
            if book["available"]:
                book["available"] = False
                print("Book is now marked borrowed")
                found = True
                return
            else:
                print("Book is already borrowed")
                return
    if not found:
        print("No books found with the name:", borrow_name)


def return_book():
    if len(books) == 0:
        print("No Books to return")
        return
    count = 0
    for book in books:
        if book["available"] == False:
            count += 1
    print("Books to be returned:", count)
    if count == 0:
        print("No books need to be returned")
        return
    i = 1
    for book in books:
        if book["available"] == False:
            print(i, ". ", book["title"], sep="")
            i += 1
    found = False
    return_name = input("Enter the name of the book to be returned: ").lower().strip()
    for book in books:
        if book["title"].lower().strip() == return_name:
            if not book["available"]:
                book["available"] = True
                print("Book has been marked as returned")
                found = True
                return
            else:
                print(book["title"], "doesnt need to be returned")
                return
    if not found:
        print("No book was found with the name:", return_name)


def search():
    while True:
        try:
            if len(books) == 0:
                print("No books available for search")
                return
            print("Would you like to search by: ")
            search = False
            i = 1
            search_choice = int(input("1. Title\n2. Author\n3. Genre\nEnter option number:  "))
            if search_choice in [1, 2, 3]:
                if search_choice == 1:
                    while True:
                        title_search = input("Enter title: ").lower().strip()
                        if title_search == "":
                            print("Title cant be empty")
                            continue
                        break
                    for book in books:
                        if title_search in book["title"].lower().strip():
                            book_info = print_book(book)
                            print(i, book_info, sep="")
                            i += 1
                            search = True
                    if not search:
                        print("No book/s found")
                        return
                elif search_choice == 2:
                    while True:
                        author_search = input("Enter name of the author: ").lower().strip()
                        if author_search == "":
                            print("Author name cant be empty")
                            continue
                        break
                    for book in books:
                        if author_search in book["author"].lower().strip():
                            book_info = print_book(book)
                            print(i, book_info, sep="")
                            i += 1
                            search = True
                    if not search:
                        print("No book/s found")
                        return
                elif search_choice == 3:
                    while True:
                        genre_search = input("Enter genre: ").lower().strip()
                        if genre_search == "":
                            print("Genre cant be empty")
                            continue
                        break
                    for book in books:
                        if genre_search in book["genre"].lower().strip():
                            book_info = print_book(book)
                            print(i, book_info, sep="")
                            i += 1
                            search = True
                    if not search:
                        print("No book/s found")
                        return
            else:
                print("Please enter number [1-3]")

        except ValueError:
            print("Invalid input type")


def delete():
    try:
        if len(books) == 0:
            print("No books available to delete")
            return
        view()
        delete_index = int(input("Enter the index of the book you would like to delete: "))
        if 0 < delete_index <= len(books):
            if books[delete_index-1]["available"]:
                books.pop(delete_index - 1)
                print("Book has been deleted")
            else:
                print("Cant delete a borrowed book")
        else:
            print("Please enter the correct index number")
    except ValueError:
        print("Invalid input type")


def main():
    add_books()
    while True:
        try:
            print("\n--- Library Management System ---")
            print("1. Add\n2. View\n3. Borrow\n4. Return\n5. Search\n6. Delete\n7. Exit\n")
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
                delete()
            elif user_choice == 7:
                print("Thank you for using Library Management System")
                break
            else:
                print("Enter a number from the menu")

        except ValueError:
            print("Invalid input type. Enter number")

main()
