N = int(input())

dp = [[0]*12 for _ in range(N+1)]

for i in range(2, 11):
    
    dp[1][i] = 1


for i in range(2, N+1):
    for j in range(1, 11):

        
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

total_sum = sum(dp[N]) % 1000000000

print(total_sum)