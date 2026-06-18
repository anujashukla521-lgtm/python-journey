# A bank account management system demonstrating encapsulation with private balance handling, along with deposit and withdrawal operations including validation checks.

class BankAccount:
    def __init__(self,account_holder,account_type,balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            return "Invalid amount"

        return "Deposited successfully"

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        else:
            return "No amount available"

        return "Withdrawal successfully"

    def display_details(self):
        print("\n====DISPLAYING INFO====")
        print(f"Account holder: {self.account_holder}")
        print(f"Account type: {self._account_type}")
        print(f"Balance: {self.__balance}")

try:
    holder = input("Enter account holder name: ")
    acc_type = input("Enter account type: ")
    balance = float(input("Enter balance: "))
    bank1 = BankAccount(holder,acc_type,balance)
    bank1.display_details()
    balance_D = float(input("Enter balance to deposit: "))
    print(bank1.deposit(balance_D))
    bank1.display_details()
    balance_W = float(input("Enter balance to withdraw: "))
    print(bank1.withdraw(balance_W))
    bank1.display_details()

except ValueError as e:
    print(e)
