N = int(input())

arr1 = sorted(list(map(int, input().split())))

M = int(input())

arr2 = list(map(int, input().split()))

for number in arr2:

    s = 0
    e = N - 1
    flag = False

    while s <= e: #교차되기전까지

        mid = (s+e)//2

        if number == arr1[mid]:
            flag = True
            break
        elif number >= arr1[mid]:
            s = mid + 1
        else:
            e = mid - 1

    if flag:
        print(1)
    else:
        print(0)

