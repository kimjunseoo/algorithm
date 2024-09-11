stair_count = int(input())

stair_value = []

for _ in range(stair_count):

    a = int(input())

    stair_value.append(a)

dp = [-1 for _ in range(stair_count)]

dp[0] = stair_value[0]
dp[1] = stair_value[1]
dp[2] = max(stair_value[0] + stair_value[1] + , stair_value[])

for i in range(3, stair_count):
    dp[i] = max(dp[i-1] + stair_value[i], dp[i-2] + stair_value[i])

print(max(dp))