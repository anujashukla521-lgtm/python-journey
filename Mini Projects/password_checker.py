# A Python mini project that checks password strength based on length, uppercase letters, lowercase letters, digits, and special characters using functions and conditional logic.

password = input("Enter password: ")
def check_length(password):
    if len(password)>=8:
        return 1
    else:
        return 0

def check_lowercase(password):
    for char in password:
        if char.islower():
            return 1 

    return 0

def check_uppercase(password):
    for char in password:
        if char.isupper():
            return 1
    return 0

def check_digit(password):
    for char in password:
        if char.isdigit():
            return 1
        
    return 0

def check_special_character(password):
    special = "@#$%&!"
    for char in password:
        if char in special:
            return 1

    return 0


strength = 0
strength += check_length(password)
strength += check_lowercase(password)
strength += check_uppercase(password)
strength += check_digit(password)
strength += check_special_character(password)

if strength <=2:
    print("Weak password")
elif strength <=4:
    print("Medium password")
else:
    print("Strong password")