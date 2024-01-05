from brain_games.game import game
from brain_games.games.even import get_answer, check_answer
from brain_games.games.even import give_question as give_question_even
from brain_games.games.even import det_answer as det_answer_even
from brain_games.games.calc import give_question as give_question_calc
from brain_games.games.calc import det_answer as det_answer_calc
from brain_games.games.gcd import give_question as give_question_gcd
from brain_games.games.gcd import det_answer as det_answer_gcd
from brain_games.games.progression import give_question as give_question_progr
from brain_games.games.progression import det_answer as det_answer_progr
from brain_games.games.prime import det_answer as det_answer_prime


def game_init(game_module):
    num_answer = False
    progr_len = None
    give_question = give_question_even
    det_answer = det_answer_even
    if game_name == 'calc':
        num_answer = True
        give_question = give_question_calc
        det_answer = det_answer_calc
    elif game_name == 'gcd':
        num_answer = True
        give_question = give_question_gcd
        det_answer = det_answer_gcd
    elif game_name == 'progr':
        num_answer = True
        progr_len = 10
        give_question = give_question_progr
        det_answer = det_answer_progr
    else:
        det_answer = det_answer_prime
    game(num_answer, progr_len, give_question=give_question,
         det_answer=det_answer, get_answer=get_answer,
         check_answer=check_answer)
