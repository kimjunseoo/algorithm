from collections import deque

N, M, V = map(int, input().split())

graph = [ [] for _ in range(N+1)]

for i in range(M):

    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

graph = [sorted(inner_array) for inner_array in graph]

ans_dfs = []
v_dfs = [ 0 for _ in range(N+1)]

ans_bfs = []
v_bfs = [ 0 for _ in range(N+1)]
q = deque()
q.append(V)

def dfs(c):
    global ans_dfs
    global v_dfs

    v_dfs[c] = 1
    ans_dfs.append(c)

    for n in graph[c]:
        if v_dfs[n] == 0:
            dfs(n)

def bfs(c):
    global q

    v_bfs[c] = 1
    ans_bfs.append(c)

    for n in graph[c]:
        if v_bfs[n] == 0:
            q.append(n)
    
while q:
    
    c = q.popleft()

    if v_bfs[c] == 0:
        bfs(c)

dfs(V)

for i in ans_dfs:
    print(i, end=" ")
print()
for i in ans_bfs:
    print(i, end=" ")