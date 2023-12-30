from brain_games.shared.error_output import main as error_output


def main(wrong_answer, rand_int_parity, name):
    if rand_int_parity is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    error_output(wrong_answer, right_answer, name)
