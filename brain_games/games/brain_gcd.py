from random import randint
from prompt import string

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer = string(f'Question: {number1} {number2}\nYour answer: ')
    correct_answer = find_gcd(number1, number2)
    return str(correct_answer), answer


def find_gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1
