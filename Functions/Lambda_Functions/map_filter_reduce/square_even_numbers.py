numbers = [7,9,2,8,5,3,7,5,1,2]

even = list(filter(lambda x: x%2==0, numbers))
print(even)

square = list(map(lambda x: x*x, even))
print(square)