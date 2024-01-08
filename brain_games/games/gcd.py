from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round(start_question, _):
    rand_num_1 = randint(0, 100)
    rand_num_2 = randint(0, 100)
    question = f'{start_question} {rand_num_1} {rand_num_2}'
    match rand_num_1 < rand_num_2:
        case True:
            min_num = rand_num_1
            max_num = rand_num_2
        case _:
            match rand_num_1 > rand_num_2:
                case True:
                    min_num = rand_num_2
                    max_num = rand_num_1
                case _:
                    right_answer = str(rand_num_1)
                    return question, right_answer
    if min_num == 0:
        gcd = max_num
    for i in range(1, min_num + 1):
        if rand_num_1 % i == 0 and rand_num_2 % i == 0:
            gcd = i
    right_answer = str(gcd)
    return question, right_answer


predicate = None
