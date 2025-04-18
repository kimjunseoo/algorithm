import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

if N <= 4:
    print(str(dp[N]))
else:
    for i in range(5, N+1):

            dp[i] = (dp[i-1] + dp[i-2]) % 15746

    print(str(dp[N]))