# Simulates a simple ATM withdrawal process with balance validation and custom error handling for invalid withdrawal amounts.

balance = 5000
try:
    amount = int(input("Enter amount to withdrawal: "))
    if amount<0 or amount>balance:
        raise ValueError("Invalid amount")
    else:
        balance-=amount
        print("Amount remaining:", balance)
except ValueError as e:
    print(e)
finally:
    print("Program ended")
