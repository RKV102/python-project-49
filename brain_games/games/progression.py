from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'
PROGR_LEN = 10


def create_progr(progr_len):
    number = randint(0, 100)
    step = randint(0, 100)
    progr = list()
    i = 0
    while i < progr_len:
        number += step
        progr.append(number)
        i += 1
    return progr


def hide_progr(progr, progr_len):
    hide_pos = choice(range(progr_len))
    hide_item = get_item(progr, hide_pos)
    set_item(progr, hide_pos, '..')
    return hide_item


def show_progr(progr, start_msg):
    msg = start_msg
    for item in progr:
        msg = f'{msg} {item}'
    print(msg)


def get_item(iterable, pos):
    return iterable[pos]


def set_item(iterable, pos, new_value):
    iterable[pos] = new_value


def give_question(progr_len, start_msg):
    progr = create_progr(progr_len)
    question_hint = hide_progr(progr, progr_len)
    show_progr(progr, start_msg)
    return question_hint


def det_answer(question_hint, _):
    return str(question_hint)


is_answer = None
