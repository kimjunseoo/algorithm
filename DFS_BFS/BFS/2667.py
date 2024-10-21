from collections import deque

N = int(input())

arr = [ list(map(int, input())) for _ in range(N) ]

#총단지수
ans_c = 0

#단지 당 아파트 수 집합
ans_arr = []

for i in range(N):
    for j in range(N):
        
        if arr[i][j] == 1:
            q = deque()
            q.append([i,j])

            #해당 인덱스 방문처리
            arr[i][j] = -1

            #총단지수
            ans_c += 1

            #단지 당 아파트 수
            ans_hc = 1

            while q:
                
                ci, cj = q.popleft()

                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj  = ci+di, cj+dj

                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                        q.append([ni, nj])
                        arr[ni][nj] = -1
                        ans_hc += 1
            

            ans_arr.append(ans_hc)
        else:
            arr[i][j] = -1

print(ans_c)
ans_arr.sort()
for a in ans_arr:
    print(a)