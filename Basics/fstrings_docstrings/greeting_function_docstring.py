# A Python function that greets the user with a personalized welcome message using f-strings and docstrings.

def greeting(n):
    '''Greets the user with welcome message'''
    print(f"Hey, {n} welcome!")

name = input("Enter name: ")
greeting(name)
print(greeting.__doc__)
