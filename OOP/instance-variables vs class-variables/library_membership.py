# A Python program that manages library member records using instance variables for member details and a class variable to maintain the total number of registered members.

class LibraryMember:
    total_members = 0
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        LibraryMember.total_members+=1

    def details(self):
        print(f"Name: {self.name} \nMember ID: {self.member_id}")


m1 = LibraryMember("Kartik",101)
m2 = LibraryMember("Sneha",201)
m3 = LibraryMember("Harshita",343)
m4 = LibraryMember("Mohit",421)

m1.details()
m2.details()
m3.details()
m4.details()
print("Total number of members:",LibraryMember.total_members)
