def recur(idx, P):
    global answer

    if idx == N:
        answer = max(answer, P)
        return

    if idx > N:
        return
    
    # 상담을 하는 경우
    recur(idx + ingre[idx][0], P + ingre[idx][1])

    # 상담을 안하는 경우
    recur(idx + 1, P)
    
N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 0

recur(0, 0)
print(answer)