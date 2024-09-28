def bfs(si, sj, ei, ej):
    global v
    global map

    q = []
    q.append([si, sj])


    while q:
        ci, cj = q.pop(0)
        
        for di, dj in [[-1,0], [0,-1], [1,0], [0,1]]:
            ni, nj = ci+di, cj+dj

            if 0<=ni<n and 0<=nj<m and map[ni][nj] == 1 and v[ni][nj] == 0:
                q.append([ni,nj])
                v[ni][nj] = v[ci][cj]+1

n,m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if 2 in map[i]:
        row = i
        col = map[i].index(2)
        break

v = [ [0]*m for _ in range(n)]
v[row][col] = 0

bfs(row, col, n-1, m-1)

#갈 수 없는 땅 -1 처리
for i in range(n):
    for j in range(m):

        if map[i][j] != 0 and v[i][j] == 0:
            v[i][j] = -1

v[row][col] = 0

for i in range(n):
    print(*v[i])