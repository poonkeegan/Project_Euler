import math
size = 1<<28
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

def divisors(factors):
    if factors == []:
        return 1
    prev = -1
    count = 1
    divisors = 1
    for factor in factors:
        if prev != factor:
            divisors *= count
            count = 2
        else:
            count += 1
        prev = factor
    divisors *= count
    return divisors

def divisors_n(n):
    return divisors(prime_factorize(n))

i = 1001
k = (1000 * 1001)/2
first = 0
while(k + i < size):
    k = k + i
    div = divisors_n(k)
    if(div > 150):
        print(k, div)
        if(first == 0 and div >= 500):
            first = k
    i = i + 1
print(first, " first with over 500 divisors")
