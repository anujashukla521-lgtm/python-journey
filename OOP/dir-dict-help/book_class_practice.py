class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

book = Book("Python Basics","John Smith",149)
book.display()
print(book.__dict__)
print(dir(book))
help(Book)
