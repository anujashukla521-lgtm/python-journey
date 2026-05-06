# A Python program that uses the time module to fetch the current system time and hour, then prints a dynamic greeting based on the time of day using conditional statements (if-elif-else).

import time 
current_time = (time.strftime('%H:%M:%S'))
hour = int(time.strftime('%H'))
print(current_time)
if (0<=hour<4):
    print("Good late night")
elif (4<=hour<12):
    print("Good morning")
elif (12<=hour<16):
    print("Good afternoon")
elif (16<=hour<=20):
    print("Good evening")
else:
    print("Good night")

