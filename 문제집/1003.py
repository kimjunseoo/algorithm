T = int(input())

dp = [ 0 for i in range(41)]

dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, 41):
    
    dp[i] = dp[i-1] + dp[i-2]

for i in range(T):

    N = int(input())

    if N == 0:
        print(1, 0)
    else:
        print(dp[N-1], dp[N])