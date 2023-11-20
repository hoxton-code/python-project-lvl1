from random import choice, randint
from prompt import string

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def check_expression(number1, number2, select_operator):
    if select_operator == '+':
        result = number1 + number2
    elif select_operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return str(result)


def make_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    select_operator = choice(OPERATORS)
    answer = string(f'Question: {number1} {select_operator} {number2}\
    \nYour answer: ')
    correct_answer = check_expression(number1, number2, select_operator)
    return correct_answer, answer
