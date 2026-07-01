class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def __add__(self,other):
        return self.balance+other

    def __sub__(self,other):
        return self.balance-other

acc = BankAccount(5000)

print(acc+1000)
print(acc-500)
