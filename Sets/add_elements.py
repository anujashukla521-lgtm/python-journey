# Takes user input and adds elements into a set dynamically.

s = set()
for i in range(5):
    elements = input("Enter elements to be added in set: ")
    s.add(elements)

print(s)
