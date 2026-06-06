from functools import reduce 

numbers = [7,9,3,6,1,5,2]
maximum_num = reduce(lambda x,y: x if x>y else y, numbers)
print(maximum_num)
