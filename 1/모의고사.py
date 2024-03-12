sut1 = [1,2,3,4,5] #5
sut2 = [2,1,2,3,2,4,2,5] #8
sut3 = [3,3,1,1,2,2,4,4,5,5] #10

answers = [1, 2, 3, 4, 5, 2, 1, 2, 3, 2, 4, 2, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answer123 = [0,0,0]
answer = []
for i in range(len(answers)):
    if answers[i] == sut1[i%5]:
        answer123[0] += 1
    if answers[i] == sut2[i%8]:
        answer123[1] += 1
    if answers[i] == sut3[i%10]:
        answer123[2] += 1

for j in range(len(answer123)):
    if (answer123[j] == max(answer123)):
        answer.append(j+1)

print(sorted(answer))