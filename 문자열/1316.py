N = int(input())

strs = []

ans = 0

for i in range(N):

    str = input()

    check = []

    for i in range(len(str)):

        if str[i] in check and str[i-1] != str[i]:
            break
        else:
            check.append(str[i])
    else:
        ans += 1

print(ans)
