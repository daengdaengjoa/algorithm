a = int(input())
time = []
b = input().split()
b1 = list(map(int,b))
# print(b1)

sorted_time = sorted(b1)
# print(sorted_time)
p=0

for j in range(len(sorted_time)):
    for i in sorted_time:
        p+=i
    sorted_time.pop()

print(p)