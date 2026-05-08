# Shows fruit prices according to the entered fruit name.

name = input("Enter fruit name: ").lower()
match name:
    case "apple":
        print("Rs. 120")
    case "banana":
        print("Rs. 40")
    case "mango":
        print("Rs. 150")
    case _:
        print("Wrong fruit name")
