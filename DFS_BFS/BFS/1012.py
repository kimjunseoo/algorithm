from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    d = deque()
    cnt = 0

    for i in range(N):         # 행
        for j in range(M):      # 열

            if farm[i][j] == 1:
                farm[i][j] = 0
                cnt += 1
                d.append([i, j])

                while d:
                    ci, cj = d.popleft()

                    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ni, nj = ci + di, cj + dj

                        if 0 <= ni < N and 0 <= nj < M and farm[ni][nj] == 1:
                            d.append([ni, nj])
                            farm[ni][nj] = 0

    print(cnt)
