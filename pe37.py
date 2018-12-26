from math import log
from primes import primes, isPrime

def truncatable(n):
    trunc = True
    digits = int(log(n,10))
    counter = 1
    while(trunc and counter <= digits):
        trunc &= isPrime[n // (10**counter)]
        counter += 1
    counter = digits
    while(trunc and counter != 0):
        trunc &= isPrime[n % (10**counter)]
        counter -= 1
    return trunc

def main():
    ttl = 0
    for i in primes:
        if truncatable(i) and i > 9:
                print(i, " is truncatable")
                ttl += i 
    return ttl
