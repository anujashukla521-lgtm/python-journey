# A Python program that stores student names and marks for three subjects, calculates total and average marks, assigns grades using a separate function, and displays formatted student records using nested loops and modular programming concepts.

def student_record():
    for student_range in range(3):
        student = input(f"Enter name of student {student_range+1}: ")
        total = 0
        for subject_range in range(3):
            marks = float(input(f"Enter marks of subject {subject_range+1} out of 100:"))
            total += marks

        average = total/3
        grade = calculate_grade(average)
        print(f"Name of student: {student}")
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print("-"*30)

def calculate_grade(score):
    if score >=80:
        return "Grade A"
    elif score >=60:
        return "Grade B"
    else:
        return "Grade C"




student_record()


