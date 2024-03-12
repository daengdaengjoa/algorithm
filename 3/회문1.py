def solution(A):
    T = int(input())
    t = 0
    q = []
    p = []
    for a1 in range(8):
        a = str(input())
        q.append(a)

    for a2 in range(8):
        p1 = []
        for a3 in range(8):
            b = q[a3][a2]
            p1.append(b)
        str1 = ''.join(str(s) for s in p1)
        p.append(str1)



    for i in range(8):
        for j in range(8 - T + 1):
            if (q[i][j:j + T] == q[i][j:j + T][::-1]):
                t += 1

    for i in range(8):
        for j in range(8 - T + 1):
            if (p[i][j:j + T] == p[i][j:j + T][::-1]):
                t += 1

    print(f'#{A} {t}')


time = 1

while time <= 10:
    solution(time)
    time += 1

