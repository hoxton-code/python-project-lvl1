from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def make_question():
    question = randint(1, 100)
    answer = string(f'Question: {question}\nYour answer: ')
    correct_answer = 'yes' if is_even(question) else 'no'
    return correct_answer, answer
