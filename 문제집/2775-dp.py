def problem(x,y):

    if dp[x][y] == -1:
        dp[x][y] = problem(x-1,y) + problem(x,y-1)

    return dp[x][y]

T = int(input())

dp = [[-1 for _ in range(15)] for _ in range(15)]

for i in range(15):
        dp[0][i] = i + 1

for i in range(15):
        dp[i][0] = 1

for _ in range(T):
      
      k = int(input())
      n = int(input())

      print(problem(k, n-1))