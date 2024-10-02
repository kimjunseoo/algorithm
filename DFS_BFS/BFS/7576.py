import sys
from collections import deque

def bfs():

    # 큐, V 생성
    q = deque()
    v = [[0]*M for _ in range(N)]

    # 초기 데이터 삽입. 토마토 count
    cnt = 0

    for i in range(N):
        for j in range(M):

            if arr[i][j] == 1:
                q.append([i,j])
                v[i][j] = 1
            elif arr[i][j] == 0:
                cnt += 1

    #bfs 시작
    while q:

        ci, cj = q.popleft()

        #6방향 탐색, 범위내, 미방문, arr[] == 0
        for di, dj in [[-1, 0],[1,0], [0,-1], [0,1]]:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
                cnt -= 1

    if cnt == 0: #모든 토마토가 익음
        return v[ci][cj] - 1
    else:
        return -1

M,N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = bfs()
sys.stdout.write(str(answer))