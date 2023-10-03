import random


def is_even(input):
    input_mod = input % 2
    if input_mod == 0:
        return True
    return False


def game(name):
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        rand_int = random.randint(0, 100)
        rand_int_parity = is_even(rand_int)
        print(f'Question: {rand_int}')
        answer = input('Your answer: ')
        if rand_int_parity is True:
            if answer == 'yes':
                print('Correct!')
                count += 1
            else:
                print(f'"{answer}" is wrong answer ;(.' +
                      'Correct answer was "yes".')
                print(f"Let's try again, {name}!")
                break
        elif answer == 'no':
            print('Correct!')
            count += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
