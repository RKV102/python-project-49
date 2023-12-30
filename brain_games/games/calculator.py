from random import choice
from brain_games.shared.gen_numbers import main as gen_numbers
from brain_games.shared.is_equal import main as is_equal
from brain_games.shared.qa import main as qa


def math_sign_selection():
    math_signs = ('+', '-', '*')
    selected_math_sign = choice(math_signs)
    return selected_math_sign


def calculation(number_1, math_sign, number_2):
    if math_sign == '+':
        calculation_result = number_1 + number_2
    elif math_sign == '-':
        calculation_result = number_1 - number_2
    else:
        calculation_result = number_1 * number_2
    return calculation_result


def game():
    count = 0
    print('What is the result of the expression?')
    while count < 3:
        number_1, number_2 = gen_numbers()
        math_sign = math_sign_selection()
        math_result = calculation(number_1, math_sign, number_2)
        answer = qa(number_1, math_sign, number_2)
        if is_equal(answer, math_result, right_msg='Correct!'):
            count += 1
        else:
            break
    is_equal(count, 3, right_msg='Congratulations!',
             wrong_handler=False)
