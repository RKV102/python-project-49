from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def give_question(start_msg):
    rand_value_1 = randint(0, 100)
    rand_value_2 = randint(0, 100)
    print(f'{start_msg} {rand_value_1} {rand_value_2}')
    return rand_value_1, rand_value_2


def det_answer(iterable, _):
    num_1 = iterable[0]
    num_2 = iterable[1]
    if num_1 < num_2:
        min_num = num_1
        gcd = num_2
    else:
        min_num = num_2
        gcd = num_1
    i = 1
    while i <= min_num:
        if num_1 % i == 0 and \
           num_2 % i == 0:
            gcd = i
        i += 1
    return str(gcd)


predicate = None
