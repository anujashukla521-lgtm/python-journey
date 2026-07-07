class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name

class Account(Bank):
    def __init__(self,bank_name,account_no,balance):
        super().__init__(bank_name)
        self.account_no = account_no
        self.balance= balance

class SavingsAccount(Account):
    def __init__(self,bank_name,account_no,balance,interest_rate):
        super().__init__(bank_name,account_no,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.balance*self.interest_rate)/100

    def display_details(self):
        print(f"Bank name: {self.bank_name}")
        print(f"Account no: {self.account_no}")
        print(f"Balance: {self.balance:.2f}")
        print(f"Interest rate: {self.interest_rate:.2f}")
        print(f"Interest amount: {self.calculate_interest():.2f}")

acc = SavingsAccount("SBI",12345,50000,2)
acc.display_details()