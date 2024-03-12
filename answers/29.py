def solution(s1, s2):
    answer = 0
    s1 = set(s1)
    s2 = set(s2)
    a = list(s1 & s2)
    answer = len(a)
    print(len(a))
    return answer