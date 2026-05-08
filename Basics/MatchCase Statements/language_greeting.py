# Prints greetings in different languages using match-case.

name = input("Enter language: ").lower()
match name:
    case "hindi":
        print("Namaste")
    case "english":
        print("Hello")
    case "french":
        print("Bonjour")
    case _:
        print("Wrong input")