try:
    user_input = input("Enter filename: ")
    user_write = input("Enter text: ").title()

    if user_input.endswith(".txt") == True:
        with open(user_input,"w")as write:
            wrote = write.write(user_write)
        with open(user_input,"r")as file:
            content = file.read()
            print(content)
    else:
        print("file must end with .txt")

except:
    print("Invalid Input")
