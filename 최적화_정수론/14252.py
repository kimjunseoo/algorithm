import math

N = int(input())

arr = list(map(int, input().split()))

cnt = 0;

for i in range(len(arr) - 1):
    for j in range(arr[i], arr[i+1]):
        if math.gcd(arr[i], 1) == 1:
            if math.gcd(arr[i+1], 1) == 1:
                cnt += 1
                break
        if j == [arr+i - 1]:
            cnt += 2

print(cnt)