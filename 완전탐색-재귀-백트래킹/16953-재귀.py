from collections import deque

A, B = map(int, input().split())

arr = [[]*10 for _ in range(10*9)]
arr[0].append(A)

ans = -1
def answer(idx, n, key):
    global ans

    if n*2 == key or int(str(n) + '1') == key:
        #print(idx, n, key)
        ans = idx


    arr[idx].append(n*2)
    arr[idx].append(int(str(n) + '1'))

    if n*2 > key and int(str(n) + '1') > key:
        return

    answer(idx+1, n*2, B)
    answer(idx+1, int(str(n) + '1'), B)


answer(1, A, B)

if ans == -1:
    print(ans)
else:
    print(ans+1)