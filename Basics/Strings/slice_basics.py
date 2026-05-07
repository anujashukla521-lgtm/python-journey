# Python programs demonstrating string slicing, reverse traversal, and substring extraction using indexing techniques.

# Program 1 : String Slicing Basics 
text = "PythonProgramming"
print(text[0:6])           # Print first 5 characters
print(text[-5:])           # Print last 6 characters
print(text[3:11])          # Print characters from index 3 to 10

# Program 2 : Sting Traversing
text = "HelloWorld"   
print(text[::2])           # Print every second chracter
print(text[::-1])          # Print the string in reverse order

# Program 3 : Half String Extraction
text = "Developer"   
length = len(text)
print(text[:length//2])    # Print the first half of the string
