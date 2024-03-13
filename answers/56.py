import math
def solution(a, b):
    answer = 0
    a1=a*(10**((math.log10(b)//1)+1))+b
    if a1 >= 2*a*b:
        answer = a1
    else:
        answer = 2*a*b
    return answer