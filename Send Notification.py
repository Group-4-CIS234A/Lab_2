def send_notification():
    print("Sending notification...")

    subject = input("Subject: ")
    message = input("Message: ")

    if not subject:
        print("Subject cannot be empty.")
        return
    if not message:
        print("Message cannot be empty.")
        return

    print("Notification sent successfully!")
    print("Subject:", subject)
    print("Message:", message)
