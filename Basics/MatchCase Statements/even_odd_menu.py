# Checks whether a number is even or odd based on user choice.

num = int(input("Enter a number: "))
choice = input("Enter a choice(even/odd): ").lower()
match choice:
    case "even":
        if num%2==0:
            print("Number is even")
        else:
            print("Number is not even")
            
    case "odd":
        if num%2!=0:
            print("Number is odd")
        else:
            print("Number is not odd")
    case _:
        print("Wrong choice")

