from functools import reduce 

numbers = [1,2,3,4,5]
add = reduce(lambda x,y: x+y, numbers)
print(add)