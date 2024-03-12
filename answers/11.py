def solution(numbers):
    answer = 0
    for number in numbers:
        answer += number
    answer = answer/len(numbers)
    return answer

def solution2(numbers):
    return sum(numbers) / len(numbers)