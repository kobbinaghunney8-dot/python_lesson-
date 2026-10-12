try:
    user_create = input("Create a file: ")
    user_write = input("Write your text: ").title()

    if user_create.endswith(".txt") == True:
        with open(user_create,"x") as create:
            with open(user_create,"w") as write:
                wrote = write.write(user_write)
        with open(user_create,"r")as file:
            content = file.read()
        print(content)
    else:
        print("File must endwith .txt")

except:
    print("Invalid Input")
