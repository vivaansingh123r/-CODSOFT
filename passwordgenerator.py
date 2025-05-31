import random
import string

# Step 1: Ask the user for the password length
length = int(input("Enter the desired password length: "))

# Step 2: Define possible characters (letters, digits, symbols)
passwordcharacters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate a random password
password = ''.join(random.choice(passwordcharacters) for _ in range(length))

# Step 4: Show the password
print("Generated password:", password)
