N, K = map(int, input().split())

def bfs(s, e):

    q = []
    q.append(s)

    v = [ 0 for _ in range(200001)]
    v[s] = 1

    while q:

        current = q.pop(0)

        if current == e:
            return v[current] - 1

        for delta in [current-1, current+1, current*2]:
            if 0<= delta <= 200000 and v[delta] == 0:
                q.append(delta)
                v[delta] = v[current] + 1

print(bfs(N, K))
