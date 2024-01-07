from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'
PROGR_LEN = None


def give_question(_, start_msg):
    rand_value_1 = randint(0, 100)
    rand_value_2 = randint(0, 100)
    signs = ('+', '-', '*')
    chosen_sign = choice(signs)
    print(f'{start_msg} {rand_value_1} {chosen_sign} {rand_value_2}')
    return rand_value_1, chosen_sign, rand_value_2


def det_answer(iterable, _):
    num_1, num_2 = get_numbers(iterable)
    sign = get_sign(iterable)
    if sign == '+':
        result = num_1 + num_2
    elif sign == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return str(result)


def get_numbers(iterable):
    return iterable[0], iterable[2]


def get_sign(iterable):
    return iterable[1]


is_answer = None
