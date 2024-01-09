from prompt import string


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    predicate = game.predicate
    print(game.DESCRIPTION)
    for i in range(3):
        question, right_answer = game.generate_round(predicate)
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
