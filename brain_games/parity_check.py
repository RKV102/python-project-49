import random


def is_even(input):
    input_mod = input % 2
    if input_mod == 0:
        return True
    return False


def error_output(wrong_answer, rand_int_parity, name):
    if rand_int_parity is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    print(f'"{wrong_answer}" is wrong answer ;(. '
          + f'Correct answer was "{right_answer}".')
    print(f"Let's try again, {name}!")


def game(name):
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        rand_int = random.randint(0, 100)
        rand_int_parity = is_even(rand_int)
        print(f'Question: {rand_int}')
        answer = input('Your answer: ')
        if rand_int_parity is True and answer == 'yes' or \
           rand_int_parity is False and answer == 'no':
            print('Correct!')
            count += 1
        else:
            error_output(answer, rand_int_parity, name)
            break
    if count == 3:
        print(f'Congratulations, {name}!')
