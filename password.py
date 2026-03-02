import string
import secrets

print("=== Password Generator ===")

while True:
    length = int(input("How many characters should your password have? "))
    lowercase = input("Include lowercase letters? (y/n) ").lower()
    uppercase = input("Include uppercase letters? (y/n) ").lower()
    symbols = input("Include symbols? (y/n) ").lower()
    numbers = input("Include numbers? (y/n) ").lower()

    characters = ""
    if lowercase == "y":
        characters += string.ascii_lowercase
    if uppercase == "y":
        characters += string.ascii_uppercase
    if symbols == "y":
        characters += "!@#$%&*"
    if numbers == "y":
        characters += string.digits

    if characters == "":
        print("You must choose at least one type of character.")
        continue
    break

password = ""

if lowercase == "y":
    password += secrets.choice(string.ascii_lowercase)

if uppercase == "y":
    password += secrets.choice(string.ascii_uppercase)

if numbers == "y":
    password += secrets.choice(string.digits)

if symbols == "y":
    password += secrets.choice("!@#$%&*")

while len(password) < length:
    password += secrets.choice(characters)

password_list = list(password)
secrets.SystemRandom().shuffle(password_list)
password = "".join(password_list)

print("Generated password:", password)

if length >= 12 and symbols == "y":
    print("Strong password")
elif length >= 8:
    print("Medium strength password")
else:
    print("Weak password")