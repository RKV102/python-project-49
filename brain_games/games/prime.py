from brain_games.games.even import give_question, det_answer, get_answer


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
PROGR_LEN = None


def is_answer(value):
    i = 2
    if value == 1:
        return False
    while i < value:
        value_mod = value % i
        if value_mod == 0:
            return False
        i += 1
    return True


give_question = give_question
det_answer = det_answer
get_answer = get_answer
