N, K = map(int, input().split())

items = []

for i in range(N):

    weight, value = map(int,input().split())

    items.append([weight, value])

print(items)