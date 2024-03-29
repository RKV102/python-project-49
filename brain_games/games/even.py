from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return not num % 2


def generate_round():
    rand_num = randint(0, 100)
    question = rand_num
    right_answer = 'yes' if is_even(rand_num) else 'no'
    return question, right_answer
