import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    # Define character pools
    lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits  # '0123456789'
    special_characters = string.punctuation  # '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all character pools combined
    all_characters = lowercase + uppercase + digits + special_characters
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password list to avoid predictable patterns (e.g., always starting with lowercase)
    random.shuffle(password)

    # Convert the list to a string and return the password
    return ''.join(password)

# Input length of password from the user
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)

if generated_password:
    print(f"Generated password: {generated_password}")
