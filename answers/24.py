def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    answer = numbers[0]*numbers[1]
    return answer
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])