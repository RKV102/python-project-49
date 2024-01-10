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
    min_num = min(rand_num_1, rand_num_2)
    max_num = max(rand_num_1, rand_num_2)
    if min_num == 0:
        return max_num
    return max(i for i in range(1, min_num + 1)
               if not bool(rand_num_1 % i)
               and not bool(rand_num_2 % i))
