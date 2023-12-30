from random import randint
from brain_games.shared.is_equal import main as is_equal
from brain_games.shared.qa import main as qa
from brain_games.shared.is_comparable import main as is_comparable


def is_even(input):
    input_mod = input % 2
    if input_mod == 0:
        return True
    return False


def game():
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        rand_int = randint(0, 100)
        rand_int_parity = is_even(rand_int)
        answer = qa(rand_int, word_answer=True)
        if is_comparable(answer, rand_int_parity, right_msg='Correct!'):
            count += 1
        else:
            break
    is_equal(count, 3, 'Congratulations!', False)
