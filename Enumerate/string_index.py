# Prints each character of a string with its position.

char = input("Enter a string: ")
for index, string in enumerate(char):
    print(f"{index} -> {string}")
