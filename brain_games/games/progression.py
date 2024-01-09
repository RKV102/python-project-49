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
    hide_pos = choice(range(PROGR_LEN))
    hide_item = str(progr[hide_pos])
    new_progr[hide_pos] = '..'
    return hide_item, new_progr


def create_question(new_progr):
    question = ' '.join(new_progr)
    return question


def generate_round(_):
    progr = create_progr()
    hide_item, new_progr = hide_item_in_progr(progr)
    question = create_question(new_progr)
    right_answer = hide_item
    return question, right_answer


predicate = None
