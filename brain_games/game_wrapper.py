from prompt import string


def game_wrapper(game):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    description = game.DESCRIPTION
    num_answer = game.NUM_ANSWER
    progr_len = game.PROGR_LEN
    give_question = game.give_question
    det_answer = game.det_answer
    get_answer = game.get_answer
    print(description)
    count = 0
    while count < 3:
        question_hint = give_question(progr_len)
        right_answer = det_answer(question_hint)
        user_answer = get_answer(num_answer)
        if user_answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{right_answer}'.")
            count = 4
        if count != 4:
            print(f'Congratulations, {user_name}!')
        else:
            print(f"Let's try again, {user_name}!")
