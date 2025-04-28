N = int(input())

arr = list(map(int, input().split()))
asc_dp = [1] * (N)
desc_dp = [0] * (N)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            asc_dp[i] = max(asc_dp[j] + 1, asc_dp[i])


for i in range(N-1, -1, -1):
    for j in range(i, N):

        if arr[i] > arr[j]:
            desc_dp[i] = max(desc_dp[j] + 1, desc_dp[i])

sum =0
for i in range(N):
    sum = max(sum,asc_dp[i]+desc_dp[i])

print(sum)