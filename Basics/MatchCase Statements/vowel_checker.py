# Checks whether the entered character is a vowel or consonant.

char = input("Enter character: ").lower()
match char:
    case 'a'|'e'|'i'|'o'|'u':
        print("It is a vowel")
    case _:
        print("It is a consonant")