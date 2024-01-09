from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    rand_num_1 = randint(0, 100)
    rand_num_2 = randint(0, 100)
    question = f'{rand_num_1} {rand_num_2}'
    gcd = find_gcd(rand_num_1, rand_num_2)
    right_answer = str(gcd)
    return question, right_answer


def find_gcd(rand_num_1, rand_num_2):
    match rand_num_1 < rand_num_2:
        case True:
            min_num = rand_num_1
            max_num = rand_num_2
        case _:
            min_num = rand_num_2
            max_num = rand_num_1
    if min_num == 0:
        gcd = max_num
    for i in range(1, min_num + 1):
        if rand_num_1 % i == 0 and rand_num_2 % i == 0:
            gcd = i
    return gcd


predicate = None
