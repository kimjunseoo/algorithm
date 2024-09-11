import sys

N = int(sys.stdin.readline())

answer = 0;

if N % 5 == 0:
    answer = N / 5
else :
    for i in range(N//5 + 1):
        na = N - (5 * i)

        if na % 3 == 0:
            answer = i + (na / 3)

if answer == 0:
    print(-1)
else :
    print(int(answer))
