def calculate_percentage(total_marks,max_marks):
    percentage = (total_marks/max_marks)*100
    return percentage

def check_pass_fail(percentage):
    return "Pass" if percentage >=33 else "Fail"