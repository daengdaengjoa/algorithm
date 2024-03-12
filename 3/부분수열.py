def sol(index, sum = 0):
    global count

    if sum == num2:
        count +=1
        return
    if index == num1:
        return

    sol(index+1, sum + data[index]) #더하기
    sol(index+1, sum) #다음으로 건너뛰기

T = int(input())

for test_case in range(1, T + 1):
    num12 = list(map(int, input().split()))
    num1 = num12[0]  # 4
    num2 = num12[1]  # 3

    count = 0
    data = list(map(int,input().split()))
    sol(0)
    print('#{} {}'.format(test_case, count))

