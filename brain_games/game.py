from brain_games.games.even import qa, greeting


def game(descr, num_answer, progr_len, **kwargs):
    user_name = greeting()
    print(descr)
    qa(user_name, num_answer, progr_len, **kwargs)
