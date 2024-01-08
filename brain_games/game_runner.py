from prompt import string


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    description = game.DESCRIPTION
    predicate = game.predicate
    generate_round = game.generate_round
    print(description)
    for i in range(3):
        question, right_answer = generate_round('Question:', predicate)
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
