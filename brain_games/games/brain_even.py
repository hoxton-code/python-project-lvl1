from random import randint
from prompt import string

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
username = string('Welcome to the Brain Games! \nMay I have your name? ')


def welcome_user(description):
    return print(f'Hello, {username}!\n{description}')


def make_question():
    random_number = generate_number()
    answer = string(f'Question: {random_number}\nYour answer: ')
    return random_number, answer


def generate_number():
    return randint(1, 100)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def run():
    welcome_user(DESCRIPTION)
    number_rounds = 3
    while number_rounds > 0:
        random_number, answer = make_question()
        correct_answer = is_even(random_number)
        if answer == correct_answer:
            number_rounds -= 1
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
