def recur(x, y):
    global white
    global blue

    if x > N:
        return
    
    if y > N:
        return
    
    if jonge[x][y] == 1:
        if jonge[x+1][y] == 1:
            recur(x+1, y)
        elif jonge[x+1][y] == 0:
            blue += 1
            recur(x+1, y)

    

    recur(x, y+1)


N = int(input())

jonge = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

print(jonge)