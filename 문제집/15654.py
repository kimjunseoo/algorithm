from itertools import permutations

N, M = map(int, input().split())

suyul = sorted([*map(int, input().split())])

answer = list(permutations(suyul, M))

for i in answer:

    for j in range(M):
        print(i[j], end=" ")
    else: 
        print()