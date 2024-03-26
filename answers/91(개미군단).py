def solution(hp):
    answer = 0
    a = hp//5
    a1 = hp%5
    b = a1//3
    c = a1%3
    answer = a+b+c
    return answer