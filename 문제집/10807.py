def recur(n):
    global pibo

    if N == 0:
        return

    if n == N+1:
        return
    
    pibo.append(pibo[n-1] + pibo[n-2])

    recur(n+1)

N = int(input())

pibo = [0, 1]

recur(2)

print(pibo[N])

#누적합 dp차이