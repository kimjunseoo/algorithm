from collections import deque

N, K = map(int, input().split())

ans = []

arr = deque()

#덱 만들기
for i in range(1, N+1):

    arr.append(i)

# 요세푸스 연산
while len(arr) != 0:
    
    # 빼기
    for _ in range(K):
        a = arr.popleft()
        arr.append(a)
    
    idx = arr.pop()
    ans.append(idx)

print(str(ans).replace('[', '<').replace(']', '>'))

