from brain_games.shared.error_output import main as error_output
from brain_games.shared.gen_numbers import main as gen_numbers


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


def game(name):
    count = 0
    print('Find the greatest common divisor of given numbers.')
    while count < 3:
        number_1, number_2 = gen_numbers()
        gcd = get_gcd(number_1, number_2)
        print(f'Question: {number_1} {number_2}')
        answer = int(input('Your answer: '))
        if answer == gcd:
            print('Correct!')
            count += 1
        else:
            error_output(answer, gcd, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')
