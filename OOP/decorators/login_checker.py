logged_in = True

def require_login(fx):
    def wrapper(*args,**kwargs):
        if logged_in:
            print("User verified")
            return fx(*args,**kwargs)
        else:
            print("Access Denied")

    return wrapper

@require_login
def view_profile():
    print("Profile opened")


view_profile()