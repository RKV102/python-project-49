from brain_games.shared.error_handler import main as error_handler
from brain_games.shared.gen_numbers import main as gen_numbers


def is_prime(number):
    i = 2
    if number == 1:
        return False
    elif number == 2:
        return True
    while i < number:
        mod_number = number % i
        if mod_number == 0:
            return False
        i += 1
    return True


def game():
    count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count < 3:
        number, _ = gen_numbers()
        prime_status = is_prime(number)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if prime_status is True and answer == 'yes' or \
           prime_status is False and answer == 'no':
            print('Correct!')
            count += 1
        else:
            error_handler(answer, prime_status)
            break
    if count == 3:
        print('Congratulations!')
