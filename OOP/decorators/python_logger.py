def logger(fx):
    def wrapper(*args,**kwargs):
        print(f"Functions name: {fx.__name__}")
        print(f"Arguments: {args}")
        result = fx(*args,**kwargs)

        print(f"Return value: {result}")
        return result
    return wrapper


@logger
def multiply(a,b):
    return a*b

@logger
def subtract(a,b):
    return a-b


ans1 = multiply(6,3)
ans2 = subtract(7,3)

