from itertools import product
from fractions import Fraction

def isCancelling(num, denom):
    if num >= denom:
        return False
    numdigs = digits(num)
    denomdigs= digits(denom)
    a, b = numdigs
    c, d = denomdigs
    if a == 0 or b == 0:
        return False
    condition = False
    if a in denomdigs:
        if a == c and d != 0:
            condition |= b / d == num / denom
        if a == d and c != 0:
            condition |= b / c == num / denom
    if b in denomdigs:
        if b == c and d != 0:
            condition |= a / d == num / denom
        if b == d and c != 0:
            condition |= a / c == num / denom
    return condition

def digits(n):
    return (n % 10, n // 10)
    
numbers = range(10,100)
fractions = product(numbers, numbers)
cancelling = []
for i in fractions:
    if isCancelling(*i):
        cancelling.append(i)
        print(i)
numerator = 1
denominator = 1
for i in cancelling:
    numerator *= i[0]
    denominator *= i[1]
    
print(Fraction(numerator, denominator))
