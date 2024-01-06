from prompt import string


def launch_game(game):
    user_name = greeting()
    description = game.DESCRIPTION
    num_answer = game.NUM_ANSWER
    progr_len = game.PROGR_LEN
    give_question = game.give_question
    det_answer = game.det_answer
    get_answer = game.get_answer
    print(description)
    count = 0
    while count < 3:
        answers = qa(user_name, num_answer, progr_len,
                     give_question=give_question,
                     det_answer=det_answer,
                     get_answer=get_answer)
        user_answer = get_user_answer(answers)
        right_answer = get_right_answer(answers)
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


def qa(user_name, num_answer, progr_len, **kwargs):
    give_question = get_func('give_question', kwargs)
    det_answer = get_func('det_answer', kwargs)
    get_answer = get_func('get_answer', kwargs)
    question_hint = give_question(progr_len)
    right_answer = det_answer(question_hint)
    user_answer = get_answer(num_answer)
    return user_answer, right_answer


def get_func(func_name, func_set):
    return func_set[func_name]


def greeting():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def get_user_answer(answers):
    return answers[0]


def get_right_answer(answers):
    return answers[1]
