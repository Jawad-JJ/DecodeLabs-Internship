import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

character_pool = ""
password_chars = []

if use_lower:
    character_pool += string.ascii_lowercase
    password_chars.append(random.choice(string.ascii_lowercase))

if use_upper:
    character_pool += string.ascii_uppercase
    password_chars.append(random.choice(string.ascii_uppercase))

if use_digits:
    character_pool += string.digits
    password_chars.append(random.choice(string.digits))

if use_symbols:
    character_pool += string.punctuation
    password_chars.append(random.choice(string.punctuation))

if not character_pool:
    print("Error: You must select at least one character type.")
elif length < len(password_chars):
    print(f"Error: Password length must be at least {len(password_chars)}.")
else:
    remaining_length = length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(random.choice(character_pool))

    random.shuffle(password_chars)
    password = "".join(password_chars)

    print("Generated Password:", password)