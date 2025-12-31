import random

# databases
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-="

# functions
def easy_password(length):
    password = ""
    for i in range(length):
        password += random.choice(letters)
    return password

def medium_password(length):
    password = ""
    for i in range(length):
        password += random.choice(letters + digits)
    return password

def hard_password(length):
    password = ""
    for i in range(length):
        password += random.choice(letters + digits + symbols)
    return password

# main function
def main():
    length = int(input("Enter password length: "))
    level = input("Choose level (easy / medium / hard): ").lower()

    if level == "easy":
        print("Password:", easy_password(length))
    elif level == "medium":
        print("Password:", medium_password(length))
    elif level == "hard":
        print("Password:", hard_password(length))
    else:
        print("Invalid level")

# loop
while True:
    choice = input("Press Enter to continue or q to quit: ")
    if choice.lower() == "q":
        break
    else:
        main()