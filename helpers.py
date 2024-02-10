import random


def generate_email():
    username = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
    random_email = f"{username}@mailforburgertest.com"
    return random_email
