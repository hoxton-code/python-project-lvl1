from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    question = randint(1, 100)
    answer = string(f'Question: {question}\nYour answer: ')
    return question, answer


def is_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'
