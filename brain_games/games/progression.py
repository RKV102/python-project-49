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


def hide_progr(progr):
    new_progr = progr[:]
    hide_pos = choice(range(PROGR_LEN))
    hide_item = progr[hide_pos]
    new_progr[hide_pos] = '..'
    return hide_item, new_progr


def show_progr(new_progr, start_msg):
    msg = start_msg
    for item in progr:
        msg = f'{msg} {item}'
    print(msg)


def give_question(start_msg):
    progr = create_progr()
    question_hint, new_progr = hide_progr(progr)
    show_progr(new_progr, start_msg)
    return question_hint


def det_answer(question_hint, _):
    return str(question_hint)


predicate = None
