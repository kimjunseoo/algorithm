K = int(input())

arr = []

for i in range(K):

    a = int(input())

    arr.append(a)

    if a == 0:
        arr.pop()
        arr.pop()
    
print(sum(arr))