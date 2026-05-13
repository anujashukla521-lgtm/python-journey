# Creates a new list containing only unique elements from the original list.

nums = [1,6,8,3,6,14,3,1,7,9]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
    
print(unique)
