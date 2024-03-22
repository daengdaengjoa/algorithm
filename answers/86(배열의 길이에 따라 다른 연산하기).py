def solution(arr, n):
    answer = []
    for i in range(1, len(arr) + 1):
        if len(arr) % 2 == 1:
            if i % 2 == 1:
                answer.append(arr[i - 1] + n)
            else:
                answer.append(arr[i - 1])

        elif len(arr) % 2 == 0:
            if i % 2 == 0:
                answer.append(arr[i - 1] + n)
            else:
                answer.append(arr[i - 1])

    return answer
