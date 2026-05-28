nums = [7,9,4,7,2,5,1]
duplicate = []
for index, numbers in enumerate(nums):
    if numbers in duplicate:
        print(f"Duplicate: {numbers} at index {index}")
    else:
        duplicate.append(numbers)