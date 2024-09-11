from itertools import combinations_with_replacement

N, M = map(int, input().split())

suyul = sorted(list(set([*map(int, input().split())])))

answer = list(combinations_with_replacement(suyul, M))

for i in answer:

    for j in range(M):
        print(i[j], end=" ")
    else: 
        print()