from brain_games.games.even import give_question, det_answer


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        num_mod = num % i
        if num_mod == 0:
            return False
    return True


give_question = give_question
det_answer = det_answer
predicate = is_prime
