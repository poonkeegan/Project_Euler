import math


def digits_of(n):
    digits = [0]*10
    if n == 0:
        digits[0] += 1
    else:
        while n != 0:
            d = n % 10
            digits[d] += 1
            n = n // 10
    return digits
     
digits = 6
found = False 
while (digits < 7) or not found:
    start = 10**(digits - 1)
    end = ((10**digits)//6) + 1
    
    for i in range (start,end):
        found = True
        multiple = 2
        while found and multiple <= 6:
            found = (digits_of(i) == digits_of(multiple*i))
            if found:
                print(multiple, i)
            multiple += 1
        if found:
            break
    digits += 1
