import random
from brain_games.shared.error_output import main as error_output
from brain_games.shared.gen_numbers import main as gen_numbers


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


def game(name):
    progression_len = 10
    count = 0
    print('What number is missing in the progression?')
    while count < 3:
        progression = get_progression(progression_len)
        position_for_cut = random.randint(0, progression_len - 1)
        progression, number_for_cut \
            = cut_progression_number(progression, position_for_cut)
        progression = turn_progression_to_str(progression)
        print(f'Question: {progression}')
        answer = int(input('Your answer: '))
        if answer == number_for_cut:
            print('Correct!')
            count += 1
        else:
            error_output(answer, number_for_cut, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')
