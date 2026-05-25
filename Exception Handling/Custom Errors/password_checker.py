try:
    password = input("Enter password: ")
    if len(password)<8:
        raise ValueError("Password should be of atleast 8 digits")
    else:
        print("Password:",password)

finally:
    print("Program over")