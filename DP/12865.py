import sys

input = sys.stdin.readline
print = sys.stdout.write


N, K = map(int, input().split())

items = []
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):

    W, V = map(int, input().split())

    items.append([W, V])

for i in range(1, len(items)+1):
    for j in range(1, K+1):

        w, v = items[i-1]

        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v )


print(str(dp[N][K]))