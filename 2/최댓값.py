a1 = []
max1 = 0
max_y = 0
max_x = 0
for i in range(9):
    a = list(map(int, input().split()))
    a1.append(a)
print(a1)
print(a1[0])
print(max(a1[0]))
for j in range(9):
    if max(a1[j]) > max1:
        max1 = max(a1[j])
        max_y = j + 1
        for p in range(9):
            if a1[j][p] == max1:
                max_x = p + 1


print(max1)
print(max_y, max_x)
