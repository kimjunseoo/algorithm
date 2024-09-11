N, M = map(int, input().split())

memo = {}
answer = []
for i in range(N):
    a, b = map(str, input().split())

    memo[a] = b


for i in range(M):
    key = input()

    answer.append(memo[key])

for i in range(M):
    print(answer[i])