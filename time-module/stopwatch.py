import time

start = input("Press enter to start: ")
start_time = time.time()

end = input("Press enter to stop: ")
end_time = time.time()

elapsed = end_time - start_time

print(f"Elapsed Time: {elapsed:.2f} seconds")