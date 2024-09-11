N = int(input())

arr = sorted(list(map(int, input().split())))

arr.insert(0, 0)

prefix = [0 for i in range(N+1)]

for i in range(1, N+1):

    prefix[i] = prefix[i-1] + arr[i]

print(sum(prefix))