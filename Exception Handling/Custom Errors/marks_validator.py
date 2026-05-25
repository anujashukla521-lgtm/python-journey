try:

    print("Enter 5 subject marks\n")
    total = 0
    for i in range(5):

        marks = float(input("Enter marks: "))

        if marks<0 or marks>100:
            raise ValueError("Marks out of range")
        else:
            total+=marks
    print("Percentage:", (total*100)/500)
                
except ValueError as e:
    print(e)

finally:
    print("Program ended")