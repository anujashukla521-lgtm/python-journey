import time

local_time = time.localtime()
formatted = time.strftime("%H:%M:%S")
print(f"Local time {formatted}")

utc_time = time.gmtime()
formatted = time.strftime("%H:%M:%S")
print(f"UTC time {formatted}")
