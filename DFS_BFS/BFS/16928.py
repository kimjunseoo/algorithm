from collections import deque

N, M = map(int, input().split())

arr = [i for i in range(101)]
sadari = {}
snake = {}
v = [-1 for _ in range(101)]
ans = 9999999
# 뱀 = -1 // 사다리 -4

# 사다리 정보 입력받기
for i in range(N):

    x,y = map(int,input().split())

    arr[x] = -4
    sadari[x] = y

# 뱀 정보 입력받기
for i in range(M):

    x,y = map(int,input().split())

    arr[x] = -1
    snake[x] = y

def bfs():
    global v
    global ans

    q = deque()
    q.append(1)
    v[1] = 0

    while q:
        
        # ci = 현재 위치
        ci = q.popleft()

        for di in [1,2,3,4,5,6]:

            # ni = 이동할 위치
            ni = ci + di

            #100을 넘어가는 경우
            if ni >= 100:
                ans = min(v[ci]+1, ans)

            if 0<ni<=100 and v[ni] == -1:
                #사다리인 경우
                if arr[ni] == -4:
                    
                    v[ni] = v[ci] + 1

                    if v[sadari[ni]] == -1:
                        q.append(sadari[ni])
                        v[sadari[ni]] = v[ci] + 1
                #뱀인 경우
                elif arr[ni] == -1:
                    
                    v[ni] = v[ci] + 1

                    if v[snake[ni]] == -1:
                        q.append(snake[ni])
                        v[snake[ni]] = v[ci] + 1
                    
                #일반 자리인 경우
                else:
                    q.append(ni)
                    v[ni] = v[ci] + 1

bfs()
print(ans)