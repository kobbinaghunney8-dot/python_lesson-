try:
    user_input = input("Enter a word: ")

    def palaindrome_checker(word):
        if word == word[::-1]:
            print("True")
        else:
            print("False")
    
    palaindrome_checker(user_input)

except ValueError:
    print("Invalid Input!!")

