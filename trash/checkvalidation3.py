
while True:
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("INVALID - Enter a nuumber...")

    print(user_input)

