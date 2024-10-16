N = int(input())

a, b = map(int, input().split())

m = int(input())

graph = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(m):

    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

ans = -1

def chonsu(x, y, idx):
    global ans

    visited[x] = 1

    if x == y:
        #print("catch", idx)
        ans = idx

    for nxt in graph[x]:

        if visited[nxt] == 0:
            chonsu(nxt, y, idx+1)

chonsu(a, b, 0)

print(ans)
