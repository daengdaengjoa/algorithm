def binary_search(array: list, target: int):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return 1
    return 0


a = int(input())
a1 = list(map(int, input().split()))
a1.sort()
b = int(input())
b1 = list(map(int, input().split()))

for k in range(b):
    print(binary_search(a1, b1[k]))
