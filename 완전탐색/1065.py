N = int(input())

answer = 0
for i in range(1, N+1):

    slice_n = list(map(int, str(i)))

    if i < 100:
        answer += 1
    elif slice_n[0] - slice_n[1] == slice_n[1] - slice_n[2]:
        answer += 1

print(answer)
    