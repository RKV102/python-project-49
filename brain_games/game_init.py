from prompt import string


def game_init(game_module):
    user_name = greeting()
    descr = game_module.DESCR
    num_answer = game_module.NUM_ANSWER
    progr_len = game_module.PROGR_LEN
    give_question = game_module.give_question
    det_answer = game_module.det_answer
    get_answer = game_module.get_answer
    check_answer = game_module.check_answer
    print(descr)
    qa(user_name, num_answer, progr_len,
       give_question=give_question, det_answer=det_answer,
       get_answer=get_answer, check_answer=check_answer)


def qa(user_name, num_answer, progr_len, **kwargs):
    give_question = get_func('give_question', kwargs)
    det_answer = get_func('det_answer', kwargs)
    get_answer = get_func('get_answer', kwargs)
    check_answer = get_func('check_answer', kwargs)
    count = 0
    while count < 3:
        question_hint = give_question(progr_len)
        right_answer = det_answer(question_hint)
        user_answer = get_answer(num_answer)
        count = check_answer(right_answer, user_answer, count)
    if count != 4:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


def get_func(func_name, func_set):
    return func_set[func_name]


def greeting():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name
