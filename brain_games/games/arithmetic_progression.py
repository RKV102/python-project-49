from random import randint
from brain_games.shared.gen_numbers import main as gen_numbers
from brain_games.shared.is_equal import main as is_equal
from brain_games.shared.qa import main as qa


def get_progression(progression_len):
    number, step = gen_numbers()
    progression = list()
    i = 0
    while i < progression_len:
        number += step
        progression.append(number)
        i += 1
    return progression


def cut_progression_number(progression, position_for_cut):
    number_for_cut = progression[position_for_cut]
    progression[position_for_cut] = '..'
    return (progression, number_for_cut)


def turn_progression_to_str(input_progression):
    progression = str(input_progression[0])
    for i in input_progression[1:]:
        progression += f' {i}'
    return progression


def game():
    progression_len = 10
    count = 0
    print('What number is missing in the progression?')
    while count < 3:
        progression = get_progression(progression_len)
        position_for_cut = randint(0, progression_len - 1)
        progression, number_for_cut \
            = cut_progression_number(progression, position_for_cut)
        progression = turn_progression_to_str(progression)
        answer = qa(progression)
        if is_equal(answer, number_for_cut, right_msg='Correct!'):
            count += 1
        else:
            break
    is_equal(count, 3, right_msg='Congratulations!',
             wrong_handler=False)
