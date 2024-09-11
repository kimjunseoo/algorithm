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

def recur(node):

    visited[node] = 1

    for nxt in graph[node]:

        if visited[nxt] == 1:
            continue

        recur(nxt)
print(graph)
recur(1)

print(sum(visited) - 1)