def count_calls(fx):
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        print(f"Function called {count} times")
        return fx(*args,**kwargs)
    return wrapper


@count_calls
def hello():
    print("Hello")

hello()
hello()
hello()