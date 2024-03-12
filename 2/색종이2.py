n = int(input())
map_array = [[0] * 100 for _ in range(100)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(b, b + 10):
        y = i
        for j in range(a, a + 10):
            x = j
            if map_array[y][x] == 0:
                map_array[y][x] = 1

sum_array = 0
for i in range(100):
    sum_array += sum(map_array[i])
print(sum_array)
