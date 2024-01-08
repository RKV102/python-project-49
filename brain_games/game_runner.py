from prompt import string


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    description = game.DESCRIPTION
    is_answer = game.is_answer
    progr_len = game.PROGR_LEN
    give_question = game.give_question
    det_answer = game.det_answer
    print(description)
    for i in range(3):
        question_hint = give_question(progr_len, 'Question:')
        right_answer = det_answer(question_hint, is_answer)
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
