from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LEN = 10


def create_progression():
    number = randint(0, 100)
    step = randint(0, 100)
    return list(range(number, number + step * PROGRESSION_LEN, step))


def generate_round():
    progression = create_progression()
    hidden_pos = choice(range(PROGRESSION_LEN))
    hidden_item = str(progression[hidden_pos])
    progression[hidden_pos] = '..'
    question = ' '.join(map(str, progression))
    right_answer = hidden_item
    return question, right_answer
