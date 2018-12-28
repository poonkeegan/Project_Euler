
def digitlen(base, n):
    l = 0
    while n != 0:
        n = n // base 
        l += 1
    return l

def dlen(n):
    return digitlen(10, n)

def blen(n):
    return digitlen(2, n)
def getdig(n, dig, b):
    shift = b ** (dig - 1)
    n = n // shift
    return n % b
def getbd(n,dig):
    return getdig(n,dig,2)
def getdd(n,dig):
    return getdig(n,dig,10)
number = 585
def dpal(n):
    l = dlen(n)
    loops = l // 2
    index = 0
    ispal = True
    while ispal and index < loops:
        ispal = getdd(n, index + 1) == getdd(n, l - index)
        index += 1
    return ispal
def bpal(n):
    l = blen(n)
    loops = l // 2
    index = 0
    ispal = True
    while ispal and index < loops:
        ispal = getbd(n,index + 1) == getbd(n, l-index)
        index += 1
    return ispal
s = 0
for i in range(1, 1000000):
    cond = dpal(i) and bpal(i)
    if cond:
        print(i, '{0:b}'.format(i))
        s += i
print(s)


