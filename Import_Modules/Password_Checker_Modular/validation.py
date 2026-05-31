def check_length(password):
    return "Length should be atleast 8 characters" if len(password)<8 else "Length is perfect"

def check_digit(password):
    for char in password:
        if char.isdigit():
            return "Password contains digits"
        
    else:
        return "No digit found"