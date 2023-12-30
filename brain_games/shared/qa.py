def main(*q, word_answer=False):
    cumulative_question = 'Question:'
    for item in q:
        cumulative_question += f' {item}'
    print(cumulative_question)
    answer = input('Your answer: ')
    if not word_answer:
        answer = int(answer)
    return answer
