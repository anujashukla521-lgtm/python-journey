# A Python OOP application that manages account balance using getters and setters, with validation for deposits, withdrawals, and negative balances.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance


    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("Balance can't be negative")
    
        self._balance = value

    def deposit(self,amount):
        if amount > 0 :
            self._balance+= amount
            return self._balance
        else:
            return "Deposit must be positive"

    def withdraw(self,amount):
        if amount<=0:
            return "Withdrawal amount must be positive"
        if amount>self._balance:
            return "Insufficient funds"
        else:
            self._balance-= amount
            return self._balance
            


amount = float(input("Enter amount: "))
obj1 = BankAccount(amount)
print("Balance:", obj1.balance)
amountD = float(input("Enter amount to deposit: "))
print(obj1.deposit(amountD))
amountW = float(input("Enter amount to withdraw: "))
print(obj1.withdraw(amountW))
print("Balance:", obj1.balance)
