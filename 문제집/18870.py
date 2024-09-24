N = int(input())

arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))

dic = {}

for i in range(len(sorted_arr)):

    if sorted_arr[i] in dic:
        continue
    else:
        dic[sorted_arr[i]] = i

for i in range(N):
    print(dic[arr[i]], end=" ")