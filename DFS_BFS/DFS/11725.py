import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]

parent = [0] * (N+1)

for i in range(N-1):

    a,b = map(int, sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)


def dfs(n):

    for nxt in tree[n]:

        if parent[nxt] == 0:
            parent[nxt] = n
            dfs(nxt)

dfs(1)

for i in range(2, N+1):
    sys.stdout.write(str(parent[i]) + '\n')