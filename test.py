a, b, c = map(int, input().split())

arr = [a, b, c]
arr.sort()

for i in range(3):
    print(arr[i], end=' ')