# Created a tuple containing only even elements from an existing tuple.

tup = (7,9,4,2,12,5,6,2)
even = []
for i in tup:
    if i%2==0 and i not in even:
        even.append(i)

even = tuple(even)
print("Even tuple:",even)
