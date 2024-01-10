from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    return all(map(lambda i: bool(num % i), range(2, num)))


def generate_round():
    rand_num = randint(0, 100)
    question = rand_num
    right_answer = 'yes' if is_prime(rand_num) else 'no'
    return question, right_answer
