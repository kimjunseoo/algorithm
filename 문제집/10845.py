from collections import deque

def _push(n):
    global arr

    arr.append(n)

def _pop():
    global arr


    if len(arr) == 0:
        print(-1)
    else:
        print(arr.popleft())



def _size():
    global arr

    print(len(arr))

def _empty():
    global arr

    if arr:
        print(0)
    else:
        print(1)
    
def _front():
    global arr

    if arr:
        print(arr[0])
    else:
        print(-1)

def _back():
    global arr

    if arr:
        print(arr[len(arr) - 1])
    else:
        print(-1)

N = int(input())

commands = [list(map(str, input().split())) for _ in range(N)]

arr = deque()


for i in range(N):
    if commands[i][0] == "push":
        _push(int(commands[i][1]))
    elif commands[i][0] == "pop":
        _pop()
    elif commands[i][0] == "size":
        _size()
    elif commands[i][0] == "empty":
        _empty()
    elif commands[i][0] == "front":
        _front()
    elif commands[i][0] == "back":
        _back()