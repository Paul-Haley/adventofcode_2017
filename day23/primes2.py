import math
n = 123700
A = [True for _ in range(0, n)]
A[0] = A[1] = False

for i in range(2, math.ceil(math.sqrt(n))):
    if A[i]:
        for j in range(i ** 2, n, i):
            A[j] = False

primes = 0
for i in range(106700, n):
    if A[i]:
        primes += 1
print(primes)
