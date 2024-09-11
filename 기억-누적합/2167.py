N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + graph[i][j]


answer = 0;
for _ in range(K):
    i,j,x,y = map(int, input().split())

    answer = prefix[x][y] - prefix[x][j-1] - prefix[i-1][y] + prefix[i-1][j-1]
    print(answer)