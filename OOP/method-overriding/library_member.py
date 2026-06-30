class Member:
    def __init__(self,name):
        self.name = name

    def borrow_book(self):
        print(f"{self.name} is borrowing a book.")

class PremiumMember(Member):
    def __init__(self,name):
        super().__init__(name)

    def borrow_book(self):
        super().borrow_book()
        print(f"{self.name} gets priority access to new arrivals.")

member = PremiumMember("Anuja Shukla")
member.borrow_book()