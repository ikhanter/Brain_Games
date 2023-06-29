import random


def gcd_game():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    if number1 > number2:
        number1, number2 = number2, number1
    for i in range(1, number1 + 1):
        if (number1 % i == 0) and (number2 % i == 0):
            result = i
    return (f'{number1} {number2}', str(result))
