class BankAccount:
    bank_name = "ABC Bank"
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_details(self):
        print(f"{self.account_holder} has account in {self.bank_name} with {self.balance} balance")

    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name 


acc1 = BankAccount("Priya",3024)
acc2 = BankAccount("Uma",1373)
acc3 = BankAccount("Tarun",92763)

acc1.display_details()
acc2.display_details()
acc3.display_details()

BankAccount.change_bank_name("XYZ Bank")
acc1.display_details()
acc2.display_details()
acc3.display_details()