import sys

N, M = map(int, sys.stdin.readline().split())

# 표 만들기
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.insert(0, [0] * N)
arr = [[0] + sublist for sublist in arr]

dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = arr[1][1]


for i in range(1, N+1):
    for j in range(1, N+1):
        
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i][j]


for k in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)