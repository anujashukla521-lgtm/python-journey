words = ["dog", "cat", "elephant", "giraffe"]
greater_words = list(filter(lambda x: len(x)>3, words))
print(greater_words)