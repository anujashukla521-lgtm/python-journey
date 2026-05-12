lst = [1,-4,7,-5,4.-5,3,7,-6]
positive = []
negative = []
for num in lst:
    if num>0:
        positive.append(num)
    else:
        negative.append(num)

print("Postive", positive)
print("Negative",negative)
