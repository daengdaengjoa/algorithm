def solution(num_list):
    answer = 0
    odd =[]
    even = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even=''.join(map(str, even))
    odd=''.join(map(str, odd))
    answer =int(odd)+int(even)
    return answer