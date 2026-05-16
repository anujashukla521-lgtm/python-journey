def greeting(n):
    '''Greets the user with welcome message'''
    print(f"Hey, {n} welcome!")

name = input("Enter name: ")
greeting(name)
print(greeting.__doc__)