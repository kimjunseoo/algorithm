from collections import defaultdict
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(N):
    element_count = defaultdict(int) 
    distinct_count = 0 

    for j in range(i, N):
        
        if element_count[arr[j]] == 0:
            distinct_count += 1
        element_count[arr[j]] += 1

        if distinct_count > 2:
            break
        
        answer = max(answer, j - i + 1)

sys.stdout.write(str(answer))
