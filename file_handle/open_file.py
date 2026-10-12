try:
    user_input = input("Enter filename: ")

    if user_input.endswith(".txt") == True:
        with open(user_input,"r") as file:
            content = file.read()
            print(content)
    else:
        print("File Must End with .txt")
except FileExistsError:
    print("Invalid Input")

