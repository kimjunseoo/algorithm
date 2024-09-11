N, M = map(int, input().split())

trees = list(map(int,input().split()))

s = 1
e = max(trees)

while s <= e: #s와 e가 교차되기 전까지
    mid  = (s+e)//2

    wood = 0

    for tree in trees:
        if tree > mid:
            wood += tree - mid

    if wood >= M:
        s = mid + 1
    elif wood < M:
        e = mid - 1

print(e)
    