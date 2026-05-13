lst = [7,9,3,6,1,7,8,2,56,23,21,64,97]
num = int(input("Enter a num: "))
found = False
for i in lst:
    if num==i:
        found = True

if found:
    print("Yes number is present")
else:
    print("No")