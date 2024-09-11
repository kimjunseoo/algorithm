N, M = map(int, input().split())

arr = list(map(int, input().split()))

tc = [list(map(int, input().split())) for _ in range(M)]

prefix = [0 for _ in range(N+1)]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]



for i in range(M):

    num_i = tc[i][0]
    num_j = tc[i][1]

    print(prefix[num_j] - prefix[num_i - 1])