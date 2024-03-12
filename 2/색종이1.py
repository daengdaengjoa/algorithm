N = int(input())

a1_a=[]
b1_b=[]
d = 0

for _ in range(N):
    a1 = []
    b1 = []
    a, b = map(int, input().split())

    for i in range(10):
        a1.append(i+a)
    for j in range(10):
        b1.append(j+b)
    a1_a.append(a1)
    b1_b.append(b1)


print(a1_a)
print(b1_b)

for i1 in range(N):
    for j1 in range(1+i1,N):
        q = len(list(set(a1_a[i1]) & set(a1_a[j1])))
        print(list(set(a1_a[i1]) & set(a1_a[j1])))
        b = len(list(set(b1_b[i1]) & set(b1_b[j1])))
        print(list(set(b1_b[i1]) & set(b1_b[j1])))
        print(q,b)
        d += q*b

print(100*N-d)