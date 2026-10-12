user_input = input("Enter your word: ")

def checker(word):
    vowels = "aeuio"
    vowels_count = 0
    consonant = "bcdfghjklmnpqrstvwxyz"
    consonant_count = 0
    for letter in word:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonant:
            consonant_count += 1

    print(f"There are {vowels_count} vowels and {consonant_count} consonant")

checker(user_input)
