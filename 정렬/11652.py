N = int(input())

dic = {}

ans_k = -1
ans_v = -1

for _ in range(N):

    a = int(input())
    
    if dic.get(a) == None:
        dic[a] = 1
    else:
        dic[a] += 1

for i in dic:
    if ans_v < dic[i]:
        ans_k = i
        ans_v = dic[i]
    elif ans_v == dic[i]:
        ans_k = min(ans_k, i)
        ans_v = dic[ans_k]

print(ans_k)