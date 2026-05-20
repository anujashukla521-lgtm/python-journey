# Checks whether a given number exists in a set.

s = {7,9,4,8,2,1,5,32,12}
num = int(input("Enter a num: "))
if num in s:
    print(f"{num} is present")
else:
    print(f"{num} is not present")
