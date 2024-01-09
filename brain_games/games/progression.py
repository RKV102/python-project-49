from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'
PROGR_LEN = 10


def create_progr():
    number = randint(0, 100)
    step = randint(0, 100)
    progr = []
    for i in range(PROGR_LEN):
        number += step
        progr.append(number)
    return progr


def hide_item_in_progr(progr):
    new_progr = progr[:]
    hidden_pos = choice(range(PROGR_LEN))
    hidden_item = str(progr[hidden_pos])
    new_progr[hidden_pos] = '..'
    return hidden_item, new_progr


def create_question(new_progr):
    question = ''
    for pos, item in enumerate(new_progr):
        if pos == 0:
            question += str(item)
        else:
            question = f'{question} {item}'
    return question


def generate_round():
    progr = create_progr()
    hidden_item, new_progr = hide_item_in_progr(progr)
    question = create_question(new_progr)
    right_answer = hidden_item
    return question, right_answer
