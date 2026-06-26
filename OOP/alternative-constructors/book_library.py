class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price


    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")

    @classmethod
    def from_string(cls,data):
        title,author,price = data.split("|")
        return cls(title,author,float(price))


book = Book.from_string("Python Basics|John Smith|499")
book.display()