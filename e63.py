

def digitpower(x, k):
    if x >= 10**((k-1)/k):
        return digitpower(x, k+1) + 1
    else:
        return 0

def amtpowers(x):
    return digitpower(x,1)

s = 0
for i in range(1,10):
    a = amtpowers(i)
    s += a
    print(i, a)
print(s)
