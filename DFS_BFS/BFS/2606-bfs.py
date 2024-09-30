from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

# grahph[1] = []
# grahph[2] = []

visited = [ 0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

q = deque()


q.append(1)

while len(q) > 0: #큐가 0이 된다면 종료

    node = q.popleft()

    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue

        q.append(nxt)

print(visited)