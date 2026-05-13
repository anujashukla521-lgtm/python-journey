nums = [7,8,3,9,1,5]
print(nums[::-1])          # using slicing
reverse = []
for i in range(-1,-len(nums)-1,-1):     # using loop
   reverse.append(nums[i])

print(reverse)