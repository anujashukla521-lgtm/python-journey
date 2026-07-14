import time

# Using for loop
def calculate_sum():
    total = 0
    for i in range(1,10000001):
        total +=i
        i+=1
    return total

start = time.time()
total = calculate_sum()
print(total)
end = time.time()

execution_time = end - start
print(f"Execution Time: {execution_time:.2f} seconds")

# Using sum() function

start = time.time()
total = sum(range(1, 10000001))
print(total)
end = time.time()

execution_time = end - start
print(f"Execution Time: {execution_time:.2f} seconds")

# Using formula
n = 10000000
start = time.time()
total = n*(n+1)//2
print(total)
end = time.time()

execution_time = end - start
print(f"Execution Time: {execution_time:.2f} seconds")