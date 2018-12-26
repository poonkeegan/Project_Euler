from math import log, floor
size = 1000000
is_prime = [False, False, True] + [True, False] * size

def init_is_prime():
    global is_prime
    for i in range(size):
        if is_prime[i]:
            for j in range(i+i, size, i):
                is_prime[j] = False
init_is_prime()

primes = [x for x in range(size) if is_prime[x]]

def filter_circular(prime):
    values = get_circular(prime)
    for i in values:
        is_prime[i] = False
    return len(values)

def get_circular(prime):
    values = [prime]
    n = cycle(prime)
    while n != prime:
        if not is_prime[n]:
            return []
        values.append(n)
        n = cycle(n)
    return values

def cycle(n):
    digits = int(floor(log(n, 10)))
    last_digit = n % 10
    return n//10 + last_digit*(10**digits)

counter = 0
for i in primes:
    counter += filter_circular(i)
print(counter)
