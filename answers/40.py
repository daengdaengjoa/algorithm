import re

def solution(my_string):
    answer = 0
    answer1 = re.sub(r'[^0-9]', '', my_string)
    answers = list(answer1)
    answer = sum(map(int, answers))
    return answer