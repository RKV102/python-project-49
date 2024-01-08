from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'
PROGR_LEN = 10


def create_progr():
    number = randint(0, 100)
    step = randint(0, 100)
    progr = list()
    i = 0
    while i < PROGR_LEN:
        number += step
        progr.append(number)
        i += 1
    return progr


def hide_progr(progr):
    hide_pos = choice(range(PROGR_LEN))
    hide_item = progr[hide_pos]
    progr[hide_pos] = '..'
    return hide_item


def show_progr(progr, start_msg):
    msg = start_msg
    for item in progr:
        msg = f'{msg} {item}'
    print(msg)


def give_question(start_msg):
    progr = create_progr()
    question_hint = hide_progr(progr)
    show_progr(progr, start_msg)
    return question_hint


def det_answer(question_hint, _):
    return str(question_hint)


predicate = None
