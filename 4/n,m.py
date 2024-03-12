r, t = map(int, input().split())


def backtracking(n, m, a):
    if len(a) == m:
        print(" ".join(map(str, a)))
        return

    for i in range(1, n + 1):
        if i not in a:
            a.append(i)
            backtracking(n, m, a)
            a.pop()


backtracking(r, t, [])
