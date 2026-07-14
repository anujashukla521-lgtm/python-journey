import time

current_time = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

print(current_time)
if 5<hour<12:
    print("Good morning")
elif 12<=hour<17:
    print("Good afternoon")
elif 17<=hour<21:
    print("Good evening")
else:
    print("Good night")