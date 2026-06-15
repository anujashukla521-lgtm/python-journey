def show_details(fx):
    def wrapper(*args,**kwargs):
        print(f"Calling add with arguments {args}")
        result = fx(*args,**kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@show_details
def add(a,b):
    return a+b

result = add(5,3)