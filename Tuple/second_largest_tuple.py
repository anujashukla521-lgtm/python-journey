tup = (7,8,3,6,9,11,54,23)
largest = tup[0]
second = tup[0]
for i in tup:
    if i>largest:
        second = largest
        largest = i
    elif i>second and second!=largest:
        second = i

print("Second largest:",second)