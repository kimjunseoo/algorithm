N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# T_answer 계산
T_answer = 0
for size in sizes:
    if size == 0:
        continue
    elif size%T == 0:
        T_answer += size//T
    elif size > T:
        T_answer += size//T+1
    elif size <= T:
        T_answer += 1 


print(T_answer)

print(N // P, N % P)