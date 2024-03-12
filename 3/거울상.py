N = int(input())
for i in range(N):
    a = input()
    b = a[::-1]
    table = str.maketrans('bdqp', 'dbpq')
    c = b.translate(table)
    print(f'#{i+1} {c}')

#
# table = str.maketrans('bdqp', 'dbpq')
# a = 'bdppq'
# b = a[::-1]
# print(b.translate(table))
