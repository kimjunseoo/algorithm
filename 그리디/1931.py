N = int(input())

meeting = [ list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x : (x[1],x[0]))

answer = 0

s = 0
e = 0

for start, end in meeting:

    if e <= start:
        s = start
        e = end
        answer += 1

print(answer)