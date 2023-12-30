import random
from brain_games.shared.error_output import main as error_output
from brain_games.shared.gen_numbers import main as gen_numbers


def math_sign_selection():
    math_signs = ('+', '-', '*')
    selected_math_sign = random.choice(math_signs)
    return selected_math_sign


def calculation(number_1, math_sign, number_2):
    if math_sign == '+':
        calculation_result = number_1 + number_2
    elif math_sign == '-':
        calculation_result = number_1 - number_2
    else:
        calculation_result = number_1 * number_2
    return calculation_result


def game(name):
    count = 0
    print('What is the result of the expression?')
    while count < 3:
        number_1, number_2 = gen_numbers()
        math_sign = math_sign_selection()
        math_result = calculation(number_1, math_sign, number_2)
        print(f'Question: {number_1} {math_sign} {number_2}')
        answer = int(input('Your answer: '))
        if answer == math_result:
            print('Correct!')
            count += 1
        else:
            error_output(answer, math_result, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')
