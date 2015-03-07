pp=2
ps=[pp]
pp+=1
ps.append(pp)
lim=raw_input("\nGenerate how many prime numbers: ")
pp+=2
while len(ps)<int(lim):
    
    test=True
    sqrtpp=(pp**0.5)
    for a in ps:
        if a>sqrtpp: break
        if pp%a==0:
            test=False
            break
    if test:
        ps.append(pp)
        print(pp)
    pp+=2
