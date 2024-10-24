T = int(input())


for _ in range(T):

    n = int(input())

    arr = []
    dp = [[0]*(n+1) for _ in range(2)]

    for i in range(2):
        arr.append(list(map(int, input().split())))
        arr[i].insert(0, 0)
    
    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]

    #DP 
    for i in range(2, n+1):
        
        dp[0][i] = max(dp[1][i-1] + arr[0][i], dp[0][i-2] + arr[0][i], dp[1][i-2] + arr[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + arr[1][i], dp[0][i-2] + arr[1][i], dp[1][i-2] + arr[1][i], dp[1][i-1])

    print(max(dp[0][n], dp[1][n], dp[0][n-1], dp[1][n-1]))