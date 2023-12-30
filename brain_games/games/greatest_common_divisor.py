from brain_games.shared.gen_numbers import main as gen_numbers
from brain_games.shared.is_equal import main as is_equal
from brain_games.shared.qa import main as qa


def get_gcd(number_1, number_2):
    min_number = get_min_number(number_1, number_2)
    i = 1
    while i <= min_number:
        if number_1 % i == 0 and \
           number_2 % i == 0:
            gcd = i
        i += 1
    return gcd


def get_min_number(number_1, number_2):
    if number_1 < number_2:
        min_number = number_1
    else:
        min_number = number_2
    return min_number


def game():
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        number_1, number_2 = gen_numbers()
        gcd = get_gcd(number_1, number_2)
        answer = qa(number_1, number_2)
        if is_equal(answer, gcd, right_msg='Correct!'):
            count += 1
        else:
            break
    is_equal(count, 3, right_msg='Congratulations!',
             wrong_handler=False)
