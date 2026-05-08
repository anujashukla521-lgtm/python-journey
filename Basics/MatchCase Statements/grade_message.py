# Displays performance messages based on student grades.

grade = input("Enter grade: ")
match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case 'D':
        print("Needs improvement")
    case 'F':
        print("Fail")
    case _:
        print("Wrong input")
