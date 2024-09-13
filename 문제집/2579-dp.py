def recur(n):
    global stair
    global dp

    if dp[n] != -1:
        return dp[n]

    dp[n] = max(recur(n-2) + stair[n], recur(n-3) + stair[n-1] + stair[n])

    return dp[n]


stair_count = int(input())

stair = [0]
dp = [ -1 for i in range(stair_count+1)]

for i in range(stair_count):

    stair.append(int(input()))

dp[0] = 0
dp[1] = stair[1]
if stair_count > 1:
    dp[2] = stair[2] + stair[1]

recur(stair_count)
print(max(dp))