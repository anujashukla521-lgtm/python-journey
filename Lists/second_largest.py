# Finds the second largest element in a list using loops and conditional logic.

lst = [7,9,3,6,8,1]
largest = 0
second = 0 
for num in lst:
    if num>largest:
        second = largest
        largest = num
    elif num>second and num!=largest:
        second = num

print("Second largest:",second)
