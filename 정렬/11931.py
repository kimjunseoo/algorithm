N = int(input())

arr = []

for i in range(N):

    num = int(input())

    arr.append(num)

arr.sort(reverse=True)

for a in arr:
    print(a)