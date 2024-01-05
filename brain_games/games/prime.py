from brain_games.games.even import give_question, get_answer, check_answer


DESCR = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_ANSWER = False
PROGR_LEN = None


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


give_question = give_question
get_answer = get_answer
check_answer = check_answer
