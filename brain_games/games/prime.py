from brain_games.games.even import greeting, qa, get_answer, give_question
from brain_games.games.even import check_answer, check_count


def det_answer(value):
    i = 2
    if value == 1:
        return 'no'
    while i < value:
        value_mod = value % i
        if value_mod == 0:
            return 'no'
        i += 1
    return 'yes'


def game():
    user_name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    qa(give_question, det_answer, get_answer,
       check_answer, check_count, user_name)
