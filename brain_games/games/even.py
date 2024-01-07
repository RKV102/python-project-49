from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_ANSWER = False
PROGR_LEN = None


def is_answer(value):
    value_mod = value % 2
    if value_mod == 0:
        return True
    return False


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


def give_question(_, start_msg):
    rand_value = gen_numbers(1)
    print(f'Question: {rand_value}')
    return rand_value


def get_answer(num_answer):
    answer = input('Your answer: ')
    if num_answer is True:
        return int(answer)
    return answer


def det_answer(question_hint, is_answer):
    if is_answer(question_hint) is True:
        return 'yes'
    return 'no'
