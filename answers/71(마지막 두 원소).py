def solution(num_list):
    a = num_list[len(num_list) - 1:len(num_list):]
    b = num_list[len(num_list) - 2:len(num_list) - 1:]
    a = a[0]
    b = b[0]
    if a > b:
        c = a - b
    else:
        c = a * 2
    num_list.append(c)
    return num_list


solution([1, 2, 3, 4, 5])
