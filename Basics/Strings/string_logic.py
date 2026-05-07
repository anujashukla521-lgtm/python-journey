# Python programs demonstrating string methods, slicing, reversing, validation, formatting, and character access techniques.

# Program 1 : Check Starting and Ending Characters
text = "Apple, banana, orange"
print(text.startswith("A"))   # Check if the string starts with 'A'
print(text.endswith("Z"))     # Check if the string ends with 'Z'

# Program 2 : Email Validation
email = "user@gmail.com"
if email.find("@")!=-1:
    print("Valid")
else:
    print("Invalid")

# Program 3 : Remove All Spaces
text = "    good morning    "
print(text.replace(" ", ""))

# Program 4 :  Reverse and Uppercase String
text = "Python"
print(text[::-1].upper())

# Program 5 : String Formatting Methods
text = "python is fun"
print(text.capitalize())    # Capitalize only the first letter       
print(text.title())         # Capitalize the first letter of each word

# Program 6 : Find Middle Character
text = "Python"
mid = len(text)//2
print(text[mid])

# Program 7 : Access String Characters
text = "HelloProgramming"
print(text[0])      # Print the first character
print(text[-1])     # Print the last character
print(text[1:-1])   # Print the string excluding first and last characters