MAX_MARKS = 500
from student_utils import calculate_percentage, check_pass_fail

def process_result():
    total = 0
    subject = 1

    while subject <= 5:
        try:
            marks = float(input(f"Enter marks: "))

            if marks < 0 or marks > 100:
                print("Marks out of range")
                continue

            total += marks
            subject += 1

        except ValueError:
            print("Invalid input")


    per = calculate_percentage(total, MAX_MARKS)
    print("Percentage", per)
    status = check_pass_fail(per)
    print(status)

process_result()