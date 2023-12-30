from brain_games.shared.error_output import main as error_handler


def main(first_num, second_num, right_msg):
    if first_num == 'yes' and second_num is True or \
       first_num == 'no' and second_num is False:
        print(right_msg)
        return True
    error_handler(first_num, second_num)
    return False
