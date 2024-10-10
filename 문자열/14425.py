N, M = map(int, input().split())

S = [ input() for _ in range(N)]

strs = [ input() for _ in range(M)]

ans = 0

for i in range(M):

    if strs[i] in S:
        ans+=1 

print(ans)