# Accesses list elements safely by handling invalid index values and non-numeric user input.

elements = [6,8,3,5,1]
try:
    index = int(input("Enter index: "))
    if index<0 or index>=len(elements):
        raise IndexError("Index out of range")
    else:
        print(elements[index])

except ValueError as e:
    print("Invalid numeric input")

except IndexError as e:
    print(e)

finally:
    print("Program over")
