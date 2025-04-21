N = int(input())

arr = list(map(int, input().split()))
dp = [1] * (N)
dp[0] = arr[0]


for i in range(N):
    for j in range(i):

        if arr[i] > arr[j]:
            dp[i] = max(arr[i] + dp[j], dp[i])

    if dp[i] == 1:
        dp[i] = arr[i]

#print(dp)
print(max(dp))