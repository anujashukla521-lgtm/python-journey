# Sorts list elements in ascending order manually without using the built-in sort() method.

nums = [4,8,2,7,11,1,6]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            nums[i],nums[j]=nums[j],nums[i]


print(nums)
