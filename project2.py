import random
import string


def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits if numbers else ''
    special = string.punctuation if special_characters else ''
    
    all_characters = letters + digits + special
    if len(all_characters) == 0:
        raise ValueError("At least one character set must be selected")

    password = []
    while len(password) < min_length:
        password.append(random.choice(all_characters))

    # Ensure the password contains at least one of each selected type
    if numbers:
        password.append(random.choice(digits))
    if special_characters:
        password.append(random.choice(special))
    
    random.shuffle(password)
    return ''.join(password)

print(password_generator(10, False))
  