# A Python mini-project that manages student records by taking student details and subject marks, calculating total marks and averages using functions, assigning grades based on performance, and displaying formatted student reports with a recursive countdown before report generation.

def input_details():
    student = []

    for student_range in range(3):

        student_name = input(f"Enter name of student {student_range+1}: ")
        student_roll = input(f"Enter roll no of student {student_range+1}: ")

        marks = []
        for marks_range in range(3):

            mark = float(input(f"Enter marks of subject {marks_range+1}: "))
            marks.append(mark)

        student.append((student_name, student_roll, tuple(marks)))

    return student

def calculate_total(marks):
    total_marks = 0
    for i in marks:
        total_marks += i
    return total_marks

def calculate_average(total_marks):
    average = total_marks/3
    return average

def assign_grade(average):
    if average>=90:
        return "A"
    elif average>=75:
        return "B"
    elif average>=64:
        return "C"
    else:
        return "D"

def countdown(n):
    if n==1:
        print(1)
    else:
        print(n)
        countdown(n-1)

students = input_details()
print("Generating result.....")
countdown(3)
for data in students:
    student_name = data[0]
    student_roll = data[1]
    marks = data[2]
    total = calculate_total(marks)
    average = calculate_average(total)
    grade = assign_grade(average)
    print("=========STUDENT REPORT========\n")
    print(f"Name: {student_name}")
    print(f"Roll no: {student_roll}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("\n===============================")




    