def recur(number, output):
    
    if number == M:
        print(output)
        return

    for i in range(1, N+1):
        recur(number+1, output+str(i)+" ")


N,M = map(int,input().split())

recur(0, "")