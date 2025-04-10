import sys
sys.setrecursionlimit(10 ** 6)


def dfs(ci, cj):

    if dp[ci][cj] == -1:
        
        dp[ci][cj] = 0
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:

            ni, nj = ci + di, cj + dj

            if arr[ni][nj] > arr[ci][cj]:
                dp[ci][cj] += dfs(ni, nj)

    return dp[ci][cj]

N, M = map(int, input().split())

arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
dp = [[-1]*(M+2) for _ in range(N+2)]

dp[1][1] = 1

print(dfs(N, M))
