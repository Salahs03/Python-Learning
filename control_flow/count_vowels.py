word = "elephant"

def count_vowels():
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    print(f"The word '{word}' has {count} vowels.")

count_vowels()

# This code counts how many vowels are in a word
