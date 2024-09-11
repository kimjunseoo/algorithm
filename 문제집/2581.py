def isPrime(a):
    if a == 1:
            return False

    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

M = int(input())

N = int(input())

primes = []

for i in range(M, N+1):
    
    if isPrime(i) == True:
        primes.append(i)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
