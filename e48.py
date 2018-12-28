s = 0
for i in range(1001): 
    s += ((i**i) % 10000000000)
print((s - 1) % 10000000000)
