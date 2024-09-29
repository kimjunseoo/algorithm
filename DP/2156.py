n = int(input())

arr = []
arr.append(0)
dp = [ 0 for _ in range(n+1)]

for i in range(n):

    a = int(input())

    arr.append(a)

dp[1] = arr[1]

# dp 
for i in range(2, n+1):

    # 가능한 경우
        # - 전 포도주와 이번 포도주를 마신다.
        # - 전전 포도주와 이번 포도주를 마신다.
        # - 전전 포도주와 전 포도주를 마시고 이번 포도주를 마시지않는다.

    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

# print(dp)
print(max(dp))