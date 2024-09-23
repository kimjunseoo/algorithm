N = int(input())

dp = [[0,0,0] for _ in range(N)]

dp[0] = [1]*3

for i in range(1, N):
    for j in range(3):

        if j == 0:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j+2]) % 9901
        elif j == 1:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 9901
        elif j == 2:
            dp[i][j] = (dp[i-1][j-2] + dp[i-1][j-1]) % 9901

print(sum(dp[N-1]) % 9901)