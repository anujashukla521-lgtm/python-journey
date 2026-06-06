from functools import reduce

numbers = [7,9,2,5,1,6,4,12]

even = list(filter(lambda x: x%2==0, numbers))
print(even)

add = reduce(lambda x,y: x+y, even)
print(add)

print("Average:",add/len(numbers)),