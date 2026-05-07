# Displays traffic instructions based on traffic light color input.

color = input("Enter traffic light color: ").lower()
match color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Slow down!")
    case "green":
        print("Go!")
    case _:
        print("Wrong input")