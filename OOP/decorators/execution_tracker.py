def tracker(fx):
    def wrapper(*args,**kwargs):
        print("Function started")
        fx()
        print("Function ended")
    return wrapper

@tracker
def function():
    print("Calculating....")

function()