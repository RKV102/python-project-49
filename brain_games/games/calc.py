from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def give_question(start_msg):
    rand_value_1 = randint(0, 100)
    rand_value_2 = randint(0, 100)
    signs = ('+', '-', '*')
    chosen_sign = choice(signs)
    print(f'{start_msg} {rand_value_1} {chosen_sign} {rand_value_2}')
    return rand_value_1, chosen_sign, rand_value_2


def det_answer(iterable, _):
    num_1 = iterable[0]
    num_2 = iterable[2]
    sign = iterable[1]
    match sign:
        case '+':
            result = num_1 + num_2
        case '-':
            result = num_1 - num_2
        case _:
            result = num_1 * num_2
    return str(result)


predicate = None
