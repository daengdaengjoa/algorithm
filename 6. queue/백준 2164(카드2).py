# N = int(input())
# queue = []
# for i in range(1,N+1):
#     queue.append(i)


# while 1:
#     queue.remove(queue[0])
#     if len(queue) == 1:
#         print(queue[0])    
#         break
#     a=queue[0]  
#     queue.remove(queue[0])
#     queue.append(a)
# 시간초과

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])