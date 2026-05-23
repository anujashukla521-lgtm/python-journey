# Day 23 Mini Project - Expense Tracker

lst = []
def add_expense():
    title = input("Enter title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    lst.append({
        "title": title,
        "amount": amount,
        "category":category
        })


def display(items):
    
    if len(items) == 0:
        print("No items found")
        return

    for expense in items:

        print(f"Title: {expense['title']}")
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['category']}")


def total_expense(items):
    total = 0
    for expense in items:
        total+=expense["amount"]
    
    return total

def highest_expense(items):

    if len(items) == 0:
        print("No expenses found")
        return

    highest = items[0]

    for expense in items:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\nHighest Expense")
    print(f"Title: {highest['title']}")
    print(f"Amount: {highest['amount']}")
    print(f"Category: {highest['category']}")


while(True):
    choice = int(input("Enter your choice:\n1. Add Expense\n2. View Expense\n3. Total Expense\n4. Highest Expense\n5. Exit\n"))
    match choice:
        case 1:
            add_expense()
        case 2:
            display(lst)
        case 3:
            print("Total expense:" total_expense(lst))
        case 4:
            highest_expense(lst)
        case 5:
            print("EXit")
            break
        case _:
            print("Invalid input")