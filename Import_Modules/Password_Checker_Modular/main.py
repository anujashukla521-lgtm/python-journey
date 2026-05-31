from validation import check_length, check_digit

password = input("Enter a password: ")
def validate(password):
    length = check_length(password)
    digit = check_digit(password)
    print(length)
    print(digit)
    print("Password is", password)


validate(password)