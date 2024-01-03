def det_answer(value):
    i = 2
    if value == 1:
        return 'no'
    while i < value:
        value_mod = value % i
        if value_mod == 0:
            return 'no'
        i += 1
    return 'yes'
