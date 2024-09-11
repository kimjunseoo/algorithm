def recur(idx):
    global answer

    if idx == N:
        return 0

    if idx > N:
        return
    

    # 상담을 하는 경우
    
    # 상담을 안하는 경우
    dp[idx] = max(recur(idx + ingre[idx][0] + ingre[idx][1], recur(idx + 1)))

N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]

dp = [ -1 for _ in range(N+1)]

answer = 0

recur(0, 0)
print(answer)