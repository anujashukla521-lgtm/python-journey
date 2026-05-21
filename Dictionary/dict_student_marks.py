# Stores student names and marks using a dictionary, then displays students, highest marks, and average marks using loops and dictionary operations.

dic = {"Harry": 98, "Ron": 87, "Hermoine": 100, "Draco": 83, "Joe": 78}
print(dic.keys())

highest = 0
for marks in dic.values():
    
    if marks > highest:
        highest = marks
    
print(highest)

total = 0
for marks in dic.values():
    total +=marks
    average = total/len(dic)

print(average)