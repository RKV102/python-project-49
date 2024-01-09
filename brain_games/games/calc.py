from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    rand_num_1 = randint(0, 100)
    rand_num_2 = randint(0, 100)
    signs = ('+', '-', '*')
    chosen_sign = choice(signs)
    question = f'{rand_num_1} {chosen_sign} {rand_num_2}'
    match chosen_sign:
        case '+':
            right_answer = str(rand_num_1 + rand_num_2)
        case '-':
            right_answer = str(rand_num_1 - rand_num_2)
        case _:
            right_answer = str(rand_num_1 * rand_num_2)
    return question, right_answer
