dic = {"Sam": 67, "Rohan": 98, "John": 76, "Mohit": 85}
try:
    name = input("Enter student name: ")
    print(f"{name}'s marks are {dic[name]}")
except KeyError:
    print("Student not found")



