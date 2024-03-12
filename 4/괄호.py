N = int(input())

for i in range(N):
    a = input()
    a1 = []
    for j in a:
        if j == "(":
            a1.append(j)
        elif j == ")":
            if a1:
                a1.pop()
            else:
                print("NO")
                break
    else:
        if not a1:
            print("YES")
        else:
            print("NO")
