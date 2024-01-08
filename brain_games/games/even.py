from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    num_mod = num % 2
    if num_mod == 0:
        return True
    return False


def generate_round(start_of_question, predicate):
    rand_num = randint(0, 100)
    question = f'{start_of_question} {rand_num}'
    if predicate(rand_num) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


predicate = is_even
