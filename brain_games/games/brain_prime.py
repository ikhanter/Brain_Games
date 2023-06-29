import random


def prime_game():
    number = random.randint(1, 9999)
    prime = 'yes'
    for i in range(2, number):
        if number % i == 0:
            prime = 'no'
            break
    return (number, prime)
