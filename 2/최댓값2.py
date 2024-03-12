max_num = 0
x = 1
y = 1

for i in range(9):

    a1 = list(map(int, input().split()))

    for j, num in enumerate(a1, 0):
        if num > max_num:
            max_num = num
            x = j + 1
            y = i + 1

print(max_num)
print(y, x)
