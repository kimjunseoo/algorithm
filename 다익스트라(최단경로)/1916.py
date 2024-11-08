import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
cost = [1e9 for _ in range(N+1)]

for i in range(M):

    S,E,C = map(int, sys.stdin.readline().split())
    graph[S].append([E, C])

start, end = map(int, sys.stdin.readline().split())


q = []
heapq.heappush(q, [0, start])
cost[start] = 0

while q:

    _c, node = heapq.heappop(q)

    if _c > cost[node]:
        continue

    for nxt, c in graph[node]:

        if cost[node] + c < cost[nxt]:
            cost[nxt] = cost[node] + c
            heapq.heappush(q, [cost[nxt], nxt]) 


sys.stdout.write(str(cost[end]) + '\n')