def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += i
    return answer



def solution2(array, n):
    return array.count(n)

print(solution([1, 1, 2, 3, 4, 5], 2))