lst = [6,8,5,9,2,3]
num = int(input("Enter num to search: "))
for i in lst:
    if i == num:
        print("Number found")
        break

else:
    print("Number not found")