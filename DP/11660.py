import sys

N, M = map(int, sys.stdin.readline().split())

# 표 만들기
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.insert(0, [0] * N)
arr = [[0] + sublist for sublist in arr]


for i in range(M):

    #누적합 테이블
    prefix = [[0]*(N+1) for _ in range(N+1)]

    x1,y1,x2,y2 = map(int, input().split())
    
    #좌표가 동일한 경우 -> 연산 필요없음
    if x1 == x2 and y1 == y2:
        sys.stdout.write(str(arr[x1][y1]) + '\n')
        continue
    
    # 누적합 테이블 초기값 설정
    prefix[x1][y1] = arr[x1][y1]
    before_x = x1
    before_y = y1
    
    for a in range(x2-x1+1):
        for b in range(y2-y1+1):
                #print("탐색 좌표: ",x1+a, y1+b)

                cur_x = x1+a
                cur_y = y1+b

                if cur_x == x1 and cur_y == y1:
                     continue

                prefix[cur_x][cur_y] = prefix[before_x][before_y] + arr[cur_x][cur_y]

                before_x = cur_x
                before_y = cur_y
                
    sys.stdout.write(str(prefix[x2][y2]) + '\n')
