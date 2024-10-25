N = int(input())

dp = [0 for _ in range(6+N)]

dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3

if N <= 4:
    print(dp[N])
else:
    for i in range(5, N+1):

        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])