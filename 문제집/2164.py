import sys
from collections import deque

N = int(sys.stdin.readline())

arr = [ i for i in range(1, N+1)]

arr = deque(arr)


while len(arr) != 1:
    
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()


sys.stdout.write(str(arr[0]))