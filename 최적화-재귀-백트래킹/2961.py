def recur(idx, sin, sseun, use) :
    global answer

    if idx == N:
        if use == 0:
            return
        result = abs(sin - sseun)
        answer = min(answer, result)
        return

    recur(idx+1, sin*ingre[idx][0], sseun+ingre[idx][1], use+1)
    recur(idx+1, sin, sseun, use)

N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 9999999999999

recur(0,1,0,0)
print(answer)