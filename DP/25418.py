A, K = map(int, input().split())

dp = [-1] * (K+1)

dp[A] = 0

for i in range(A, K+1):

    if i+1 <= K and dp[i+1] == -1:
        dp[i+1] = dp[i] + 1
    if i*2 <= K and dp[i*2] == -1:
        dp[i*2] = dp[i] + 1

print(dp[K])

