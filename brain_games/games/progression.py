from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LEN = 10


def create_progression():
    number = randint(0, 100)
    step = randint(0, 100)
    progression = []
    for i in range(PROGRESSION_LEN):
        number += step
        progression.append(number)
    return progression


def hide_item_in_progression(progression):
    new_progression = progression[:]
    hidden_pos = choice(range(PROGRESSION_LEN))
    hidden_item = str(progression[hidden_pos])
    new_progression[hidden_pos] = '..'
    return hidden_item, new_progression


def create_question(new_progression):
    question = ''
    for pos, item in enumerate(new_progression):
        if pos == 0:
            question += str(item)
        else:
            question = f'{question} {item}'
    return question


def generate_round():
    progression = create_progression()
    hidden_item, new_progression = hide_item_in_progression(progression)
    question = create_question(new_progression)
    right_answer = hidden_item
    return question, right_answer
