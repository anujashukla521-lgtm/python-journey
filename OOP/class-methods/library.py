# A Python program that uses a class method to modify a shared class attribute, allowing all library book objects to reflect the updated library name.

class Book:
    library_name = "Central Library"
    def __init__(self,title):
        self.title = title

    def display(self):
        print(f"Title: {self.title}\nLibrary Name: {self.library_name}")


    @classmethod
    def change_library_name(cls,new_name):
        cls.library_name = new_name

b1 = Book("Python")
b2 = Book("DSA")
b3 = Book("OS")

b1.display()
b2.display()
b3.display()

Book.change_library_name("Public Library")
b1.display()
b2.display()
b3.display()
