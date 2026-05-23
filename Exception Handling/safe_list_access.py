lst = ["Harry","Ron","Hermoine","Luna","Draco"]

try:
    index = int(input("Enter index: "))
    print(lst[index])

except ValueError:
    print("Non-numeric input")
except IndexError:
    print("Invalid index")