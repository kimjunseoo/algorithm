N = input()
start = N
cnt = 0

if start == '0':
    print(1)
    exit()
    


while True:

    if int(N) < 10:
        N = '0' + N

    s = int(N[0]) + int(N[1])

    if s >= 10:
        s = str(s)
        s = s[1]
    elif s < 10:
        s = str(s)
    
    if N[1] == '0':
        N = s
    else:
        N = N[1] + s

    cnt += 1

    if N == start:
        print(cnt)
        break