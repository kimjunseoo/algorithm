from collections import deque
import sys

def _add(x):
    global arr

    if arr.count(x) > 0:
        return
    else:
        arr.append(x)

def _remove(x):

    global arr

    if arr.count(x) > 0:
        arr.remove(x)


def _check(x):

    global arr

    if arr.count(x) > 0:
        sys.stdout.write('1' + '\n')
    else:
        sys.stdout.write('0' + '\n')

def _toggle(x):

    global arr

    if arr.count(x) > 0:
        arr.remove(x)
    else:
        arr.append(x)

def _all():

    global arr

    arr.clear()

    for i in range(1, 21):
        arr.append(i)

def _empty():

    global arr

    arr.clear()


M = int(input())

arr = deque()

for i in range(M):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "add":
        _add(int(command[1]))
    elif command[0] == "remove":
        _remove(int(command[1]))
    elif command[0] == "check":
        _check(int(command[1]))
    elif command[0] == "toggle":
        _toggle(int(command[1]))
    elif command[0] == "all":
        _all()
    elif command[0] == "empty":
        _empty()