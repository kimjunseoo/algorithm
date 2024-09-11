N = int(input())

arr1 = list(map(int,input().split()))

M = int(input())

arr2 = list(map(int,input().split()))

arr3 = arr2.copy()

answer = {a: 0 for a in arr2}

arr2.sort()

for number in arr1:

    s = 0
    e = N-1
    flag = False

    while s <= e:
        mid = (s+e)//2

        if arr2[mid] == number: #만약 중간값이 number와 같다면
            flag = True
            break
        if arr2[mid] > number:
            e = mid - 1
        if arr2[mid] < number:
            s = mid + 1
    
    if flag:
        answer[number] += 1

for i in arr3:
    print(answer[i], end=" ")