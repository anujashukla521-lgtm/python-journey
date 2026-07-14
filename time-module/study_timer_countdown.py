import time

hours = int(input("Enter hour: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = hours*3600 + minutes*60 + seconds

while total_seconds>=0:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    total_seconds-=1
print("Time finished")


