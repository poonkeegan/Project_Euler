import math

def fib(n):
    least = 0
    biggest  = 1
    end = 1
    for i in range(n - 1):
        end = least + biggest
        least = biggest
        biggest = end
    return end

#print(len(str(fib(4781))))
def perim():
    a = []
    for i in range(1, 1001, 1):
        for j in range(1, i + 1, 1):
            c = math.sqrt(i*i + j*j)
            if c.is_integer() and (i + j + c) <= 1000:
                a.append(i + j + c)
    a.sort()
    counter = 0
    for i in range(len(a) - 1):
        if(counter > 5):
            print(a[i], counter)
        if(a[i + 1] == a[i]):
            counter += 1
        else:
            counter = 0

def collatz(n):
    counter = 1
    while(n != 1):
        if(n%2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        counter += 1
    return counter
'''
largest = 0
val = 0
for i in range(1, 1000000, 1):
    x = collatz(i)
    if(largest < x):
        largest = x
        val = i
print(val)
'''


def distinct_powers(n1, n2):
    powers = set()
    size = max(n1**n2, n2**n1)
    for a in range(2, n1 + 1, 1):
        for b in range(2, n2 + 1, 1):
            num = a**b
            powers.add(num)
    return len(powers)
#print(distinct_powers(100,100))

def largest_prod():
    grid = []
    for i in range(20):
        grid.append(input().split())
    for i in range(20):
        for j in range(20):
            grid[i][j] = int(grid[i][j])
    for i in range(20):
        print(grid[i])
    print(searchallcol(grid))
    print(searchallrow(grid))
    print(searchalldiagright(grid))
    print(searchalldiagleft(grid))

def searchallcol(grid):
    maxval = 0
    for j in range(20):
        curr = searchcol(j, grid)
        if maxval < curr:
            maxval = curr
    return maxval

def searchcol(j, grid):
    maxval = 0
    for i in range(17):
        curr = 1
        for x in range(4):
            curr *= grid[i + x][j]
        if maxval < curr:
            maxval = curr
    return maxval

def searchallrow(grid):
    maxval = 0
    for i in range(20):
        curr = searchrow(i, grid)
        if maxval < curr:
            maxval = curr
    return maxval

def searchrow(i, grid):
    maxval = 0
    for j in range(17):
        curr = 1
        for x in range(4):
            curr *= grid[i][j + x]
        if maxval < curr:
            maxval = curr
    return maxval

def searchalldiagright(grid):
    maxval = 0
    for i in range(17):
        curr = searchdiagright(i, grid)
        if maxval < curr:
            maxval = curr
    return maxval

def searchdiagright(i, grid):
    maxval = 0
    for j in range(17):
        curr = 1
        for x in range(4):
            curr *= grid[i + x][j + x]
        if maxval < curr:
            maxval = curr
    return maxval

def searchalldiagleft(grid):
    maxval = 0
    for i in range(3, 20):
        curr = searchdiagleft(i, grid)
        if maxval < curr:
            maxval = curr
    return maxval

def searchdiagleft(i, grid):
    maxval = 0
    for j in range(17):
        curr = 1
        for x in range(4):
            curr *= grid[i - x][j + x]
        if maxval < curr:
            maxval = curr
    return maxval
    
def large_sum():
    sumval = 0
    for x in range(100):
        curr = int(input()) 
        sumval += curr
    return sumval

def fifth_power():
    sumval = 0
    for x in range(2, 500000):
        if test_power(x):
            sumval += x
            print(sumval)

def test_power(n):
    orig = n
    sumval = 0
    while n > 0:
        curr = n % 10
        sumval += curr*curr*curr*curr*curr
        n //= 10
    return sumval == orig

def p40():
    string = ""
    length = 0
    num = 0
    while length < 1000001:
        curr = str(num)
        length += len(curr)
        string += curr
        num += 1
    print(length)
    print(int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000]))
p40()