try:
    user_input = input("Create a fliename: ")

    if user_input.endswith(".txt"):
        with open(user_input,"x")as create:
            create.close()
            print("File Create Sucessesfully")
    else:
        print("File Must Endwith .txt")

except ValueError:
    print("Invalid Input")
