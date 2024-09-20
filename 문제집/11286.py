import heapq

N = int(input())

abs_hp = []
answer = []
for i in range(N):

    x = int(input())

    if x == 0 and len(abs_hp) == 0 :
        answer.append(0)
    elif x == 0:
        answer.append(heapq.heappop(abs_hp))
    elif x:
        heapq.heappush(abs_hp, (abs(x), x))

for i in range(len(answer)):

    if answer[i] == 0:
        print(0)
    else:
        print(answer[i][1])