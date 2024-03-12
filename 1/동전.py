
a, b = map(int, input().split())
a1_a =[]
for i in range(a):
    a1 = int(input())
    a1_a.append(a1)

a1_a.reverse()
p=0
for j in range(len(a1_a)):
    if b >= a1_a[j]:
        p += b//a1_a[j]
        b = b%a1_a[j]
    if b==0:
        break

print(p)