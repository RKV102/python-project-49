from brain_games.games.even import greeting, qa, get_answer, gen_numbers
from brain_games.games.even import check_answer, check_count


def give_question(_):
    rand_value_1, rand_value_2 = gen_numbers(2)
    print(f'Question: {rand_value_1} {rand_value_2}')
    return rand_value_1, rand_value_2


def get_min_num(num_1, num_2):
    if num_1 < num_2:
        min_num = num_1
    else:
        min_num = num_2
    return min_num


def get_first_num(iterable):
    return iterable[0]


def get_second_num(iterable):
    return iterable[1]


def det_answer(iterable):
    num_1 = get_first_num(iterable)
    num_2 = get_second_num(iterable)
    min_num = get_min_num(num_1, num_2)
    i = 1
    while i <= min_num:
        if num_1 % i == 0 and \
           num_2 % i == 0:
            gcd = i
        i += 1
    return gcd


def game():
    user_name = greeting()
    print('Find the greatest common divisor of given numbers.')
    qa(give_question, det_answer, get_answer, check_answer,
       check_count, user_name, num_answer=True)
