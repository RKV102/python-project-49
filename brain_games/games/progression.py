from brain_games.games.even import greeting, qa, get_answer, gen_numbers
from brain_games.games.even import check_answer, check_count
from random import choice


def make_progr(progr_len):
    number, step = gen_numbers(2)
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


def show_progr(progr):
    question = 'Question:'
    for item in progr:
        question = f'{question} {item}'
    print(question)


def get_item(iterable, pos):
    return iterable[pos]


def set_item(iterable, pos, new_value):
    iterable[pos] = new_value


def give_question(progr_len):
    progr = make_progr(progr_len)
    question_hint = hide_progr(progr, progr_len)
    show_progr(progr)
    return question_hint


def det_answer(question_hint):
    return question_hint


def game():
    progr_len = 10
    user_name = greeting()
    print('What number is missing in the progression?')
    qa(give_question, det_answer, get_answer, check_answer,
       check_count, user_name, num_answer=True, progr_len=progr_len)
