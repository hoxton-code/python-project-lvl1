from random import randint
from prompt import string

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def make_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    answer = string(f'Question: {number1} {number2}\nYour answer: ')
    return (number1, number2), answer

def find_gcd(numbers):
    number1, number2 = numbers
    while number2:
        number1, number2 = number2, number1 % number2
    return number1

def is_correct_answer(number):
    return str(find_gcd(number))