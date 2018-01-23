def isPrime(i):
    for odd in range(3, i//2, 2):
        if i % odd == 0:
            return False
    return True

primes = 0
for i in range(106700, 123700, 17):
    if isPrime(i):
        primes += 1
        #print("we got one!", i)
print("primes = ", primes)

