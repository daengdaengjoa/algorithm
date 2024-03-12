def solution(num_list):
    answer = 1
    ams = 0
    for num in num_list:
        answer *= num
    if sum(num_list)**2 > answer:
        ams = 1
    else:
        ams = 0
    return ams