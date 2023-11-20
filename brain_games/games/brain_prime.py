from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(number / 2 + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def make_question():
    number = randint(2, 1000)
    answer = string(f'Question: {number}\nYour answer: ')
    correct_answer = str(is_prime(number))
    return correct_answer, answer
