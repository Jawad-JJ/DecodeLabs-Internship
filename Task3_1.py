import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

length = int(input("Enter the password length (e.g., 8): "))

print("Generated Password:", generate_password(length))