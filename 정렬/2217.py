N = int(input())

ropes = []
ans = []

for i in range(N):
    ropes.append(int(input()))

ropes.sort()


for i in range(N):

    ans.append(ropes[i] * (N - i))

print(max(ans))