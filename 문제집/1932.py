N = int(input())

arr = []
dp = [ [-1]*N for _ in range(N)]


for i in range(N):

    nums = list(map(int, input().split()))

    arr.append(nums)

dp[0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i+1):

        if i+1 == j:
            #dp[4][3] = dp[3][2] + arr[4][3]
            dp[i][j] = dp[i-1][j-1] + arr[i][j]
        else:
            #dp[4][3] = dp[3][2] + arr[4][3] or dp[3][3] + arr[4][3]
            dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])

print(max(dp[N-1]))