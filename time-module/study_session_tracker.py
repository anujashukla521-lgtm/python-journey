import time

start_time = None
total_time = 0

while True:
    try:
        choice = int(input("""
        1. Start Study Session
        2. End Study Session
        3. Show Total Study Time
        4. Exit
        """))
        match choice:
            case 1:
                if start_time is None:
                    start_time = time.time()
                    print(f"Study session started at {time.strftime('%H:%M:%S')}")
                else:
                    print("Study session already running")
            
            case 2:
                if start_time is not None:
                    end_time = time.time()
                    duration = end_time - start_time
                    total_time+=duration
                    start_time = None
                    print("Study session ended.")
                    print(f"Session duration: {int(duration)} seconds")
                else:
                    print("No study session is running.")

            case 3:
                total_seconds = int(total_time)
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60
                print(f"Total study time: {hours:02}:{minutes:02}:{seconds:02}")
            case 4:
                print("Thank you for using the Study Timer!")
                break
            case _:
                print("Invalid input")

    except ValueError:
        print("Please enter a valid number")

