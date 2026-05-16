# A program that accepts marks of three subjects, calculates total and average marks, and displays the result using formatted output.

marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
total = marks1+marks2+marks3
average = total/3
print(f"Total Marks: {total:.0f}\nAverage: {average:.2f}")
