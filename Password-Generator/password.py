import random
import string

length = int(input("Enter password length: "))

use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print("\nGenerated Password:", password)
