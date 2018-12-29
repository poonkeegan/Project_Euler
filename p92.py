def chain(n):
    while True:
        new = 0
        while n != 0:
            new += (n % 10)**2
            n //= 10
        n = new
        if n == 1 or n == 89:
            return n
count = 0
for x in range(1, 10000000):
    if chain(x) == 89:
        count += 1
print(count)