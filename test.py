def isPrime(a):

    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


if isPrime(11) == True:
    print("YEA")