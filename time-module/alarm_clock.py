import time

hour = int(input("Enter hour(24-hour format): "))
minute = int(input("Enter minute: "))

if hour not in range(24) or minute not in range(60):
    print("Invalid Time!")
    exit()

print(f"Alarm set for {hour:02}:{minute:02}")
print("Waiting...")

while True:
    current_hour = int(time.strftime("%H"))
    current_minute = int(time.strftime("%M"))

    if current_hour == hour and current_minute == minute:
        print("Wake Up!")
        print("Current time:",time.strftime('%H:%M'))
        break
    
    time.sleep(1)