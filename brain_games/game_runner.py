from prompt import string


ROUNDS_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    for i in range(ROUNDS_COUNT):
        question, right_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{right_answer}'.\n"
                  + f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
