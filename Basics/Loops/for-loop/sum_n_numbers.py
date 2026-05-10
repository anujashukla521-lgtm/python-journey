# Calculates the sum of numbers from 1 to n using a loop.

num = int(input("Enter num: "))
total = 0
for k in range(1,num+1):
    total = total+k
print(total)
