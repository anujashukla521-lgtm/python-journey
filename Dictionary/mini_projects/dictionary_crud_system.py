# A menu-driven Python program that performs Create, Read, Update, and Delete (CRUD) operations on a dictionary using loops, match-case, functions, and user input.

def countdown(n):
    if n<=0:
        return
    if n == 1:
        print(1)
    else:
        print(n)
        countdown(n-1)

dic = {}
while True:

    
    choice = int(input("Enter\n1-Add item\n2- Update item\n3-Delete item\n4-Search item\n5-Display\n6-Exit : "))
    match choice:
        case 1:
            key = input("Enter key to store: ")
            value = input("Enter value to store: ")
            dic[key] = value
            print("Item added")
        
        case 2:
            key = input("Enter key to update: ")
            new_value = input("Enter new value: ")
            if key in dic:
                dic[key] = new_value
                print("Key updated")
            else:
                print("Key not found")

        case 3:
            key = input("Enter key to delete: ")
            if key in dic:
                del dic[key]
                print("Key deleted")
            else:
                print("Key not found")
        
        case 4:
            item = input("Enter item to search: ")
            if item in dic:
                print(f"{item} is present")
            else:
                print(f"{item} is absent")
        case 5:
            print("Displaying dictionary....")
            countdown(3)
            for key,value in dic.items():
                print(key,":",value)
                
        case 6:
            print("Exit")
            break
        case _:
            print("Wrong choice")
        

