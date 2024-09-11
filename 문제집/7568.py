N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

count = [ 0 for _ in range(N)]

for i in range(N):

    for j in range(N):

        if i == j:
            continue

        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count[i] += 1

for i in range(N):
    print(count[i] + 1, end=" ")