def d(n):

    answer = n

    for i in list(str(n)):
        answer  += int(i)

    return answer

for i in range(1, 10001):

    ss = 0 

    for j in range(i//2, i):

        if d(j) == i:
            ss += 1
    
    if ss == 0:
        print(i)