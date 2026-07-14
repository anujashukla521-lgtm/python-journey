import time

input("Press enter to start: ")
start_time = time.time()

sentence = input("Enter a sentence: ")

input("Press enter to end: ")
end_time = time.time()

elapsed_time = end_time - start_time

word_count = len(sentence.split())
minutes = elapsed_time/60
if minutes>0:
    wpm = word_count/minutes
else:
    wpm = 0
    
print("\nTyping test results")
print("---------------------")
print(f"Sentence  :{sentence}")
print(f"Time taken  :{elapsed_time:.2f}")
print(f"Words types :{word_count}")
print(f"Typing speed  :{wpm:.2f}")
