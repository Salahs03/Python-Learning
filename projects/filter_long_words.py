words = ["apple", "dog", "banana", "sun"]
long_words = []

def find_long_words():
    for word in words:
        if len(word) > 4:
            long_words.append(word)
    print("Long words:", long_words)

find_long_words()

# This code filters words longer than 4 letters
