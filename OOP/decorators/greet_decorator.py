def welcome_message(fx):
    def wrapper(*args,**kwargs):
        print("Welcome to the program")
        fx()
    return wrapper


@welcome_message
def greet():
    print("Hello, Anuja")

greet()