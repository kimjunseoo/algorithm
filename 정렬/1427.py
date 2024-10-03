import sys

arr = list(map(int,input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    sys.stdout.write(str(arr[i]))