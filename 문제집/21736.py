def bfs(si, sj, ei, ej):
    global answer

    q = []
    q.append([si, sj])
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        
        if arr[ci][cj] == 'P':
            answer += 1

        for di, dj in [[-1,0], [0,-1], [1,0], [0,1]]:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and  0<=nj<M and arr[ni][nj] != 'X' and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = 1

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
answer = 0


for i in range(N):
    if "I" in arr[i]:
        row = i
        col = arr[i].index("I")
        break

bfs(row,col,N-1,M-1)

if answer == 0:
    print('TT')
else:
    print(answer)