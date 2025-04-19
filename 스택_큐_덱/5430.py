from collections import deque

T = int(input())

for _ in range(T):

    reverse = False

    p = list(input())

    n = int(input())

    arr = input().rstrip()[1:-1]
    arr = deque(arr.split(",")) if arr else deque()

    error = False

    for func in p:
        if func == 'D':
            if not arr:
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()
        elif func == 'R':
            reverse = not reverse

    if error:
        print("error")
    else:
        result = list(map(int, reversed(arr))) if reverse else list(map(int, arr))
        print(f"[{','.join(map(str, result))}]")
