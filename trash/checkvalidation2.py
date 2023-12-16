list_valid_chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

while True:
    user_input = input("Enter just one letter: ")

    if user_input not in list_valid_chars:
        print("INALID: enter just letter of the alphabet")
    else:
        break

print(f"You entered {user_input}")