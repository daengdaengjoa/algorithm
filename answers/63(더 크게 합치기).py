def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    c=a+b
    d=b+a
    answer = int(c)
    if d > c:
        answer = int(d)
    return answer