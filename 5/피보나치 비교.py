i=1
def fibonacci(n):
    global i
    if n == 0 or n == 1:
        return 1
    else:
        i += 1
        return fibonacci(n-1) + fibonacci(n-2)

# def fibonacci2(n):
#     if n == 0 or n == 1:

print(fibonacci(5),i)