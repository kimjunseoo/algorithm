from itertools import permutations, product
import sys

N, M = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, N+1)]

for a in product(nums, repeat=M):
    
    sys.stdout.write(str(" ".join(map(str, a))) + '\n')