arr = [[0]*100 for _ in range(100)]

n = int(input())

for i in range(n):

    x, y = map(int, input().split())

    for a in range(10):
        for b in range(10):
            arr[y-1+a][x-1+b] = 1
    
total_sum = sum(sum(row) for row in arr)
print(total_sum)