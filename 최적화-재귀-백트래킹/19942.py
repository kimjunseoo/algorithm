def recur(idx, d, t, j, v, price, output) :
    global answer
    global output_result

    if d>=md and t >=mt and j>=mj and v>=mv: 
        answer = min(answer, price)
        if answer == price :
            output_result = output
        return
    
    if idx > N -1:
        return
    
    # 재료를 더하지 않는 경우
    recur(idx+1, d, t, j, v, price, output)

    # 재료를 더하는 경우
    recur(idx+1, d+foods[idx][0], t+foods[idx][2], j+foods[idx][1], v+foods[idx][3], price+foods[idx][4], output+str(idx+1)+" ")


N = int(input())

md, mj, mt, mv = map(int, input().split())

foods = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999
output_result = ""

recur(0,0,0,0,0,0,"")


if answer != 99999999999:
    print(answer)
    print(output_result)
else :
    print(-1)
