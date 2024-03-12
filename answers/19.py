def solution(dot):
    if dot[0] * dot[1] > 0:
        answer = 1 + 2*(dot[0] < 0)
    else:
        answer = 2 + 2*(dot[0] > 0)
    return answer

# def solution(dot):
#     quad = [(3,2),(4,1)]
#     return quad[dot[0] > 0][dot[1] > 0]