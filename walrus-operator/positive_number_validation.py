number = 0

while (number:= int(input("Enter a positive number: ")))<=0:
    print("Invalid Input! Please enter a postitive number")

print(f"Valid number {number}")