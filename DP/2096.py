import sys

N = int(sys.stdin.readline())

a,b,c  = list(map(int, input().split()))

max_dp = [a,b,c]
min_dp = [a,b,c]


for i in range(N-1):
    d, e, f = map(int, sys.stdin.readline().split())

    max_a = max(max_dp[0], max_dp[1]) + d
    max_b = max(max_dp[0], max_dp[1], max_dp[2]) + e
    max_c = max(max_dp[1], max_dp[2]) + f

    min_a = min(min_dp[0], min_dp[1]) + d
    min_b = min(min_dp[0], min_dp[1], min_dp[2]) + e
    min_c = min(min_dp[1], min_dp[2]) + f

    max_dp = [max_a, max_b, max_c]
    min_dp = [min_a, min_b, min_c]

print(max(max_dp), min(min_dp))