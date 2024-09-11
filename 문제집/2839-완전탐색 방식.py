import sys
sys.setrecursionlimit(5001)

def recur(count, weight):
    global answer

    if weight == N:
        answer = min(answer, count)
        return
    
    if weight > N:
        return

    #3키로를 넣는 경우
    recur(count + 1, weight + 3)

    #5키로를 넣는 경우
    recur(count + 1, weight + 5) 


N = int(sys.stdin.readline())

answer = 9999999

recur(0,0)

if answer == 9999999:
    sys.stdout.write(str(-1))
else :
    sys.stdout.write(str(answer))