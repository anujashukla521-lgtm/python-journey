import time

try:
    while True:
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)

except KeyboardInterrupt:
    print("Clock stopped!")

