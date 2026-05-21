# Takes a sentence from the user and counts how many times each word appears using a dictionary and frequency counting logic.

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

for word,count in word_count.items():
    print(word,":",count)