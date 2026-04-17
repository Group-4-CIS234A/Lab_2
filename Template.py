def choose_template():
    print("Choose a template")
    print("1. Hello message")
    print("2. Reminder message")
    print("3. Goodbye message")

    choice = input("Pick a number: ")

    if choice == "1":
        return "Hello, hope you're doing well."
    elif choice == "2":
        return "Just a reminder about our meeting."
    elif choice == "3":
        return "Goodbye, talk soon."
    else:
        print("Not a valid choice.")
        return None


# quick test
if __name__ == "__main__":
    t = choose_template()
    if t:
        print("You picked:", t)