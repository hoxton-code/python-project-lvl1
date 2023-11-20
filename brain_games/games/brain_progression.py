from random import randint
from prompt import string

DESCRIPTION = 'What number is missing in the progression?'


def create_progression():
    step = randint(2, 10)
    length_progression = step * 10
    start_number = randint(1, length_progression)
    end_number = start_number + length_progression
    progression = list(range(start_number, end_number, step))
    correct_answer = progression.pop(step - 1)
    progression.insert(step - 1, '..')
    result = ''
    for i in progression:
        result += str(i) + ' '
    result.rstrip()
    return result, correct_answer


def make_question():
    progression, correct_answer = create_progression()
    answer = string(f'Question: {progression}\nYour answer: ')
    return str(correct_answer), answer
