from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    question = randint(1, 100)
    answer = string(f'Question: {question}\nYour answer: ')
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, answer
