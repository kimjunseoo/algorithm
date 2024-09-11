from collections import deque

N, K = map(int, input().split())

dq = deque()
answer = []

for i in range(1, N+1):
    dq.append(i)

while len(dq) != 0:

    dq.rotate(-K + 1)

    a = dq.popleft()

    answer.append(a)


for i in range(N):

    if N == 1:
        print("<"+str(answer[i])+">")
    else: 
        if i == 0:
            print("<" + str(answer[i]), end=", ")
        elif i == N-1:
            print(str(answer[i])+">")
        else:
            print(answer[i], end=", ")