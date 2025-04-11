N = int(input())

arr = list(map(int, input().split()))
dp = [1] * (N+2)
dp[0] = 1
dp2 = [1] * (N+2)
dp2[0] = 1

#증가 
for i in range(N-1):

    if arr[i] <= arr[i+1]:
        dp[i+1] = dp[i] + 1
    
#print(dp)
#감소
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        dp2[i+1] = dp2[i] + 1

#print(dp2)
print(max(max(dp), max(dp2)))
