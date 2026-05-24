books = {}
def add_book():
    book = input("Enter book name: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))

    books[book] ={
        
            "Author name": author,
            "Quantity": quantity
        
    }

def issue_book(book):
    book_name = input("Enter book name to issue: ")
    if book_name in book:
        if book[book_name]["Quantity"]>0:
            book[book_name]["Quantity"]-=1
            print("Book issued successfully")
            print(f"Remaining quantity:{book[book_name]['Quantity']}")
        else:
            print("Unavailable")
    else:
        print("Book not found")

def return_book(book):
    book_name = input("Enter book name to return: ")
    if book_name in book:
        
        book[book_name]["Quantity"]+=1
        print("Book returned")
        print(f"Updated book quantity: {book[book_name]['Quantity']}")
    else:
        print("Wrong book name")


def view_book(book):
    for library in book:

        print("Book name:", library)
        print(f"Author name: {book[library]['Author name']}")
        print(f"Quantity: {book[library]['Quantity']}")

def search_book(book):
    book_name = input("Enter book name to search: ")
    if book_name in book:
        print("Book Found\n")
        print("Book name:", book_name)
        print(f"Author name: {book[book_name]['Author name']}")
        print(f"Quantity: {book[book_name]['Quantity']}")
    else:
        print("Book not found")

while True:
    choice = int(input("Enter your choice:\n1-Add Book\n2-Issue Book\n3-Return Book\n4-View Available Book\n5-Search Book\n6-Exit\n"))
    match choice:
        case 1:
            add_book()
        case 2:
            issue_book(books)
        case 3:
            return_book(books)
        case 4:
            view_book(books)
        case 5:
            search_book(books)
        case 6:
            print("Exit")
            break
        case _:
            print("Invalid input")