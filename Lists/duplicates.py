nums = [8,9,4,7,1,8,2,6,3,8,1,5,8,1,5]
checked = []
for i in nums:
    if nums.count(i)>1 and i not in checked:
        print(i)

    checked.append(i)