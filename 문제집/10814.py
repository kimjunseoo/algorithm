N = int(input())

arr = []

for i in range(N):
    a = list(map(str, input().split()))
    a.append(i)
    arr.append(a)

arr.sort(key=lambda x: (int(x[0]), x[2]))

for i in range(N):
    print(arr[i][0] + ' ' + arr[i][1])