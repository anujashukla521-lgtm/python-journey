email = input("Enter email: ")

if len(parts:=email.split("@"))==2 and parts[0] and parts[1]:
    print("Domain: ",parts[1])
else:
    print("Invalid email")