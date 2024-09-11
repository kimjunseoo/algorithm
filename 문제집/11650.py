import sys

N = int(sys.stdin.readline().strip())

loca = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

loca.sort()

for i in range(N):
    sys.stdout.write(str(loca[i][0]) + " " + str(loca[i][1]) + '\n')