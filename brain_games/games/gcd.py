from brain_games.games.even import gen_numbers


DESCR = 'Find the greatest common divisor of given numbers.'
NUM_ANSWER = True
PROGR_LEN = None


def give_question(_):
    rand_value_1, rand_value_2 = gen_numbers(2)
    print(f'Question: {rand_value_1} {rand_value_2}')
    return rand_value_1, rand_value_2


def get_min_max_num(num_1, num_2):
    if num_1 < num_2:
        min_num = num_1
        max_num = num_2
    else:
        min_num = num_2
        max_num = num_1
    return min_num, max_num


def get_first_num(iterable):
    return iterable[0]


def get_second_num(iterable):
    return iterable[1]


def det_answer(iterable):
    num_1 = get_first_num(iterable)
    num_2 = get_second_num(iterable)
    min_num, gcd = get_min_max_num(num_1, num_2)
    i = 1
    while i <= min_num:
        if num_1 % i == 0 and \
           num_2 % i == 0:
            gcd = i
        i += 1
    return gcd
