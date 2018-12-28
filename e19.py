weekday = 2
year = 1901
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysinmonth(month):
    if month != 1:
        return monthdays[month]
    elif (year % 100) == 0:
        if (year % 400) == 0:
            return monthdays[month] + 1
        else:
            return monthdays[month]
    elif (year % 4) == 0:
        return monthdays[month] + 1
    else:
        return monthdays[month]

def sundaymonth(month):
    days = daysinmonth(month)
    global weekday
    retval = weekday == 0
    weekday += days
    weekday = weekday % 7
    return retval

sumsun = 0
for i in range(100):
    for j in range(12):
        if sundaymonth(j):
            sumsun += 1
    year += 1
print(sumsun)
