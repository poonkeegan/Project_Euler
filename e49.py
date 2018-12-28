import math
size = 1<<15
#32 crashes, 28 takes a while and works
sieve = [False, True] * (size>>1)
sieve[2] = True 
sieve[1] = False
primes = [2]
limit = math.ceil(math.sqrt(size))
print("Loading primes")
for i in range(3,limit):
    if sieve[i]:
        for j in range(2*i, size, i):
            sieve[j] = 0
print("Sieve complete")
for i in range(size):
    if sieve[i]:
        primes.append(i)
print("Done loading")
def prime_factorize(n):
    if n < 2:
        return []
    global primes
    i = 0
    factors = []
    while(n > 1):
        while n % primes[i] == 0:
            factors.append(primes[i])
            n = n//primes[i]
        i += 1
    return factors

index = 0
while primes[index] < 10000:
    if(primes[index] >= 1000):
        print(primes[index])
    index += 1
