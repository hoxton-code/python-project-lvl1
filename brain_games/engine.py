from prompt import string


def run(game):
    number_rounds = 3
    username = string('Welcome to the Brain Games! \nMay I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)
    while number_rounds > 0:
        correct_answer, answer = game.make_question()
        if answer == correct_answer:
            number_rounds -= 1
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{correct_answer}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
