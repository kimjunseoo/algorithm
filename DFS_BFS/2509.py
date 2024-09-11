from collections import deque

Y, X = map(int, input().split())

graph = [list(input().restip()) for _ in range(Y)]

maxi = 0

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 'L':
            