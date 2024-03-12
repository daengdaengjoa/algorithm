
num = []
x = 100

while x != 1000:
    q = tuple(map(str, str(x)))
    if (q[0] != q[1] and
        q[1] != q[2] and
        q[2] != q[0] and '0' not in q):
        num.append(q)
    x += 1

print(num)


N = int(input())
for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    bb = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= bb  # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s):
            num.remove(num[i])
            bb += 1
        elif (ball != b):
            num.remove(num[i])
            bb += 1

print(len(num))