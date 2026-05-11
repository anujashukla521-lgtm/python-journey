def count(st):
    vowel_count = 0
    consonant_count = 0
    for i in st:
        if i.isalpha():
            if i in "aeiouAEIOU":
                vowel_count = vowel_count+1
            else:
                consonant_count = consonant_count+1
    return vowel_count, consonant_count


text = input("Enter string: ")
v,c= count(text)
print("Vowels:",v)
print("Consonants:",c)

        
