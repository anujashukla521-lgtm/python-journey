class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_data(self):
        print(f"Name: {self.name}\nAge: {self.age}")

    @classmethod
    def from_dict(cls,data):
        name = data["name"]
        age = data["age"]
        return cls(name,int(age))

p1 = Person.from_dict({"name": "Anuja Shukla", "age": 200})
p1.display_data()