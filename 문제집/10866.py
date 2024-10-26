from collections import deque

def _push_front(x):
    global d

    d.appendleft(x)

def _push_back(x):
    global d

    d.append(x)

def _pop_front():
    global d

    if len(d) == 0:
        print(-1)
    else:
        print(d.popleft())

def _pop_back():
    global d

    if len(d) == 0:
        print(-1)
    else:
        print(d.pop())

def _size():
    global d

    print(len(d))

def _empty():
    global d

    if len(d) == 0:
        print(1)
    else:
        print(0)

def _front():
    global d

    if len(d) == 0:
        print(-1)
    else:

        x = d.popleft()

        print(x)
        d.appendleft(x)

def _back():
    global d

    if len(d) == 0:
        print(-1)
    else:

        x = d.pop()

        print(x)
        d.append(x)

N = int(input())
commands = [list(map(str, input().split())) for _ in range(N)]

d = deque()


for i in range(N):
    if commands[i][0] == "push_front":
        _push_front(int(commands[i][1]))
    elif commands[i][0] == "push_back":
        _push_back(int(commands[i][1]))
    elif commands[i][0] == "pop_front":
        _pop_front()
    elif commands[i][0] == "pop_back":
        _pop_back()
    elif commands[i][0] == "size":
        _size()
    elif commands[i][0] == "empty":
        _empty()
    elif commands[i][0] == "front":
        _front()
    elif commands[i][0] == "back":
        _back()
