s = input().upper()

arr = {}

for st in s:
    if st in arr and arr[st] >= 1:
        arr[st] += 1
    else:
        arr[st] = 1

ans = -1
ans_k = ''

for key in arr:

    if arr[key] > ans:
        ans = arr[key]
        ans_key = key

    elif arr[key] == ans:
        ans_key = '?'

print(ans_key)