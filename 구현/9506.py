def getMyDivisor(n):

    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)

    return divisorsList

while True:

    n = int(input())

    if n == -1:
        break

    divisorsList = getMyDivisor(n)

    if sum(divisorsList) - n == n:
        print(f"{n} = {' + '.join(map(str, divisorsList[:-1]))}")
    else:
        print(f"{n} is NOT perfect.")