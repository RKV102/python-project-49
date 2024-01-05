from brain_games.greeting import greeting
from brain_games.qa import qa


def game_init(game_module):
    user_name = greeting()
    descr = game_module.DESCR
    num_answer = game_module.NUM_ANSWER
    progr_len = game_module.PROGR_LEN
    give_question = game_module.give_question
    det_answer = game_module.det_answer
    get_answer = game_module.get_answer
    check_answer = game_module.check_answer
    print(descr)
    qa(user_name, num_answer, progr_len,
       give_question=give_question, det_answer=det_answer,
       get_answer=get_answer, check_answer=check_answer)
