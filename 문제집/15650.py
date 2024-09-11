def recur(idx, count, stx):
    global suyul
    global answer
    # print(idx, count, stx)

    if count == M:
        answer.append(stx)
        return
    
    if idx >= N:
        return
    
    #같은 숫자를 추가하는 경우
    recur(idx, count + 1, stx + str(suyul[idx + 1]) + " ")

    #숫자를 추가하는 경우
    recur(idx + 1, count + 1, stx + str(suyul[idx+ 1]) + " ")

    #숫자를 추가하지 않는 경우
    recur(idx + 1, count, stx)

N, M = map(int, input().split())

suyul = [i for i in range(N+1)]

answer = []

recur(0,0,"")

result = sorted(list(set(answer)))

for i in result:
    print(i)
