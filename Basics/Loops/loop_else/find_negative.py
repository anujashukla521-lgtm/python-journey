# A Python program that searches a list for the first negative number using a for loop with else, printing the result if found.

lst = [6,8,1,5,2,4,-6,9,12]

for i in lst:
    if i<0:
        print(i)
        break

else:
    print("No negative numbers found")
