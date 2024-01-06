from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_ANSWER = False
PROGR_LEN = None


def det_answer(value):
    value_mod = value % 2
    if value_mod == 0:
        return 'yes'
    return 'no'


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
