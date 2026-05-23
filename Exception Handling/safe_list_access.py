# Allows the user to access an element from a list using an index and safely handles invalid inputs and out-of-range index errors.

lst = ["Harry","Ron","Hermoine","Luna","Draco"]

try:
    index = int(input("Enter index: "))
    print(lst[index])

except ValueError:
    print("Non-numeric input")
except IndexError:
    print("Invalid index")
