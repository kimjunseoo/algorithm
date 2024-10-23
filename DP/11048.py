N, M = map(int, input().split())

dp = [[-1]*(M+1) for _ in range(N+1)]

arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0]*(M+1))
arr = [[0] + sublist for sublist in arr]

dp[1][1] = arr[1][1]

for x in range(1, N+1):
    for y in range(1, M+1):

        if x == 1 and y == 1:
            continue

        dp[x][y] = max(dp[x-1][y]+arr[x][y], dp[x][y-1]+arr[x][y], dp[x-1][y-1]+arr[x][y])


print(dp[N][M])