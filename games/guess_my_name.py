def guess_check():
    secret_word = "Melly"
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        user_input = input("Guess: ")
        guess_count += 1

    if user_input == secret_word:
        print("Yhhh You Won!!")
    else:
        print("Oh Sorry You Lose!!")

guess_check()
