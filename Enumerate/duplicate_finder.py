# Finds duplicate elements and prints their positions.

nums = [7,9,4,7,2,5,1]
seen_nums = []
for index, numbers in enumerate(nums):
    if numbers in seen_nums:
        print(f"Duplicate: {numbers} at index {index}")
    else:
        seen_nums.append(numbers)
