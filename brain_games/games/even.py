from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
PROGR_LEN = None


def is_answer(value):
    value_mod = value % 2
    if value_mod == 0:
        return True
    return False


def give_question(_, start_msg):
    rand_value = randint(0, 100)
    print(f'{start_msg} {rand_value}')
    return rand_value


def det_answer(question_hint, is_answer):
    if is_answer(question_hint):
        return 'yes'
    return 'no'
