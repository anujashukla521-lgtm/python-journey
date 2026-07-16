while True:
    print("--------------------")
    print("DISPLAYING MENU")
    print("1. Add")
    print("2. Delete")
    print("3. Update")
    print("4. Exit")

    if (choice:=int(input("Enter a choice: ")))==4:
        break

    if choice == 1:
        print("Adding...")

    elif choice == 2:
        print("Deleting...")

    elif choice == 3:
        print("Updating...")

    else:
        print("Invalid Choice")

print("Program Ended")