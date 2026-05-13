tup1 = (6,8,1,49,12,45,21)
tup2 = (21,12,45,32,8,76)
common = []
for i in tup1:
    for j in tup2:
        if i==j:
            if i not in common:
                common.append(i)


common = tuple(common)
print(common)

