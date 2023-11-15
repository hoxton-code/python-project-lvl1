from prompt import string


def run(game):
    number_rounds = 3
    username = string('Welcome to the Brain Games! \nMay I have your name? ')
    print(game.DESCRIPTION)
    while number_rounds > 0:
        question, answer = game.make_question()
        correct_answer = game.is_correct_answer(question)
        if answer == correct_answer:
            number_rounds -= 1
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
