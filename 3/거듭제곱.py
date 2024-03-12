
for _ in range(10) :
    T = int(input())
    r, t = map(int, input().split())

    def fa(n, m) :
        if m == 0 :
            return 1
        elif m != 0:
            a = fa(n,m-1)*n
            return a


    q = fa(r, t)

    print(f'#{T} {q}')