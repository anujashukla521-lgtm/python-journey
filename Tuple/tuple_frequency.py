tup = (1,2,3,7,1,5,2)
checked = []
for i in tup:
    if i not in checked:
        print(i,"->",tup.count(i))
        checked.append(i)
