from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(number / 2 + 1)):
        if number % i == 0:
            return False
    return True


def make_question():
    number = randint(2, 1000)
    answer = string(f'Question: {number}\nYour answer: ')
    correct_answer = 'yes' if is_prime(number) else 'no'
    return correct_answer, answer
