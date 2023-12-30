from brain_games.shared.gen_numbers import main as gen_numbers
from brain_games.shared.is_equal import main as is_equal
from brain_games.shared.qa import main as qa
from brain_games.shared.is_comparable import main as is_comparable


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
        answer = qa(number, word_answer=True)
        if is_comparable(answer, prime_status, right_msg='Correct!'):
            count += 1
        else:
            break
    is_equal(count, 3, 'Congratulations!', False)
