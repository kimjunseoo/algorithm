import heapq

N = int(input())

heap = []

answer = []

for i in range(N):

    a = int(input())

    if a == 0:
        if len(heap) == 0:
            answer.append(0)
        else:
            num = heapq.heappop(heap)
            answer.append(num)
    else:
        heapq.heappush(heap, a)

for i in range(len(answer)):
    print(answer[i])