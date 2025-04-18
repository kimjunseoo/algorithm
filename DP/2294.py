n, k = map(int, input().split())

coins = set()

for _ in range(n):

    v = int(input())

    coins.add(v)

INF = k+1
dp = [INF] * (k+1)

dp[0] = 0

for coin in coins:

    for j in range(1, k+1):

        if j - coin >= 0:

            dp[j] = min(dp[j], dp[j-coin] + 1)

ans = dp[k]

if ans == INF:
    ans = -1

print(ans)
