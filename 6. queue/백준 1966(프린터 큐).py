from collections import deque

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    deque1 = deque(list(map(int, input().split())))
    dd = 0

    while deque1:
        best = max(deque1)
        front = deque1.popleft()
        b -= 1

        if best == front:
            dd += 1
            if b < 0:
                print(dd)
                break

        else:
            deque1.append(front)
            if b < 0:
                b = len(deque1) - 1
