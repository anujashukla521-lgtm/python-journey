# A Python program that uses a while loop to calculate the sum of numbers from 0 to the user-entered number.

num = int(input("Enter a num: "))
sum = 0
count = 0
while count<=num:
    sum +=count
    count +=1
    
print("Sum: ",sum)
