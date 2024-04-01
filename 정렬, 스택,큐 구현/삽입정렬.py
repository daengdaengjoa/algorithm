import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(nums)
print(nums)

def Insertion_Sort(A):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j -1]
                print(A)

    return A

Insertion_Sort(nums)

print(nums)

nums.sort()