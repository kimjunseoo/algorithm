import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.insert(0, [0]*(N+1))

for sub_arr in arr:
    sub_arr.insert(0, 0)

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

prefix_sum[1][1] = arr[1][1]

#누적합 구하기
for y in range(1, N+1):
        for x in range(1, N+1):

            if x == 1:
                prefix_sum[y][x] = prefix_sum[y-1][N] + arr[y][x]
            else:
                prefix_sum[y][x] = prefix_sum[y][x-1] + arr[y][x]

for i in range(M):

    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    if x1 == x2 and y1 == y2:
        print(arr[x1][y1])
    elif x1 == 1 and y1 == 1:
        print((prefix_sum[x2][y2] - prefix_sum[x1][y1]) + 1) 
    else:   
        print(prefix_sum[x2][y2] - prefix_sum[x1][y1]) 