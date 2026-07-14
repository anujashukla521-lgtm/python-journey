import time

questions = ["Who developed Python Programming Language?","Which type of Programming does Python support?","Is Python case sensitive when dealing with identifiers?","What is the correct extension of the Python file?","Is Python code compiled or interpreted?"]
for index,ques in enumerate(questions,start=1):
    start_time = time.time()
    print(f"{index}: {ques}")
    answer = input("Enter answer: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    if elapsed_time > 10:
        print("Time out!")
    else:
        print("Answer received")