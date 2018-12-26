from math import log
from itertools import permutations
from primes import primes, isPrime, primeCheck

def pandigital(n):
    digits = int(log(n,10))
    string = str(n)
    for i in range(1, digits+2):
        if string.find(str(i)) == -1:
            return False
    return True

def main(n):
    perms = permutations(range(n,0,-1))
    for i in perms:
        num = 0
        for j in i:
            num *= 10
            num += j
        if primeCheck(num):
            print(num, " is prime")

for i in range(9,0,-1):
    main(i)
