from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

components = 0

for i in range(M):

    U, V = map(int,input().split())

    graph[U].append(V)
    graph[V].append(U)

q = deque()

q.append(1)

def recur(node):

    visited[node] = 1

    for nxt in graph[node]:

        if visited[nxt] == 1:
            continue
        
        recur(nxt)

for i in range(1, N+1):
    if visited[i] == 0:
        recur(i)
        components += 1

print(components)