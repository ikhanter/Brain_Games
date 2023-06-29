import random


def generate_number():
    number = random.randint(1, 99999)
    even = 'yes' if number % 2 == 0 else 'no'
    return (number, even)
