from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]


dfs_visited = [ 0 for _ in range(N+1)]
bfs_visited = [ 0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

dfs = []
bfs = []

def recur(node):

    dfs_visited[node] = 1
    dfs.append(node)

    for nxt in graph[node]:

        if dfs_visited[nxt] == 1:
            continue

        recur(nxt)

recur(V)

q = deque()

q.append(V)

while len(q) > 0: #큐가 0이 된다면 종료

    node = q.popleft()

    bfs_visited[node] = 1
    bfs.append(node)

    for nxt in graph[node]:
        if bfs_visited[nxt] == 1:
            continue

        q.append(nxt)

print(dfs)
print(bfs)