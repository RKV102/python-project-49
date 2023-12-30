from brain_games.shared.error_output import main as error_output


def main(first_num, second_num, right_msg, wrong_handler=True):
    if first_num == second_num:
        print(right_msg)
        return True
    if wrong_handler:
        error_output(first_num, second_num)
    return False
