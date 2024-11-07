from collections import deque
import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
dist = [1e9 for _ in range(N+1)]

for _ in range(M):

    A,B,C = map(int, sys.stdin.readline().split())
    graph[A].append([B, C])

#BFS 

q = []
heapq.heappush(q, [0, start])
dist[start] = 0


while q:

    # heapq.heapify(q)
    _w, node = heapq.heappop(q)

    for nxt, weight in graph[node]:
        # 1. 각각의 노트에 값을 업데이트
        # 2. 만약 여러 경로가 존재한다면 min() 비교
        # 3. 시작점으로부터 거리를 봐서, 짧은 순서대로 탐색 (오염 방지)
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])


for i in range(1, N+1):
    if dist[i] == 1e9:
        sys.stdout.write('INF' + '\n')
    else:
        sys.stdout.write(str(dist[i]) + '\n')