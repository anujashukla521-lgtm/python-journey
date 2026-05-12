num = [7,9,3,7,9,1,5,1,1,7,3,7,5,2]
checked = []
for i in num:
    if i not in checked:
        print(i,"->",num.count(i))
        checked.append(i)

        
         
