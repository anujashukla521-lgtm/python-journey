class Library:
    def __init__(self):
        self.name = "Central Library"
        self.books = ["Maths","Phy","Biology","Science"]

    def __len__(self):
        i = 0
        for book in self.books:
            i = i + 1
        return i


obj = Library()
print(obj.name)
print("Books:",len(obj))