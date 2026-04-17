def create_account():
    print("Create Account")
    username = input("New username: ")
    password = input("New password: ")

    try:
        open("users.txt", "x").close()
    except:
        pass

    with open("users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username:
                print("That username already exists.")
                return

    with open("users.txt", "a") as f:
        f.write(username + "," + password + "\n")

    print("Account created.")