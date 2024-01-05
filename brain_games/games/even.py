from prompt import string
from random import randint


def greeting():
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def det_answer(value):
    value_mod = value % 2
    if value_mod == 0:
        return 'yes'
    return 'no'


def get_func(func_name, func_set):
    return func_set[func_name]


def qa(user_name, num_answer, progr_len, **kwargs):
    give_question = get_func('give_question', kwargs)
    det_answer = get_func('det_answer', kwargs)
    get_answer = get_func('get_answer', kwargs)
    check_answer = get_func('check_answer', kwargs)
    check_count = get_func('check_count', kwargs)
    count = 0
    while count < 3:
        question_hint = give_question(progr_len)
        right_answer = det_answer(question_hint)
        user_answer = get_answer(num_answer)
        count = check_answer(right_answer, user_answer, count)
    check_count(count, user_name)


def gen_numbers(count):
    if count == 1:
        rand_value = randint(0, 100)
        return rand_value
    rand_values = []
    i = 0
    while i < count:
        rand_value = randint(0, 100)
        rand_values.append(rand_value)
        i += 1
    return rand_values


def give_question(_):
    rand_value = gen_numbers(1)
    print(f'Question: {rand_value}')
    return rand_value


def get_answer(num_answer):
    answer = input('Your answer: ')
    if num_answer is True:
        return int(answer)
    return answer


def check_answer(right_answer, user_answer, count):
    if right_answer == user_answer:
        print('Correct!')
        count += 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              + f"Correct answer was '{right_answer}'.")
        count = 4
    return count


def check_count(count, user_name):
    if count != 4:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")
