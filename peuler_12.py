


n = {}
n[0] = 0
n[1] = 3
n[2] = 3
n[3] = 5
n[4] = 4
n[5] = 4
n[6] = 3
n[7] = 5
n[8] = 5
n[9] = 4
n[10] = 3
n[11] = 6
n[12] = 6
n[13] = 8
n[14] = 8
n[15] = 7
n[16] = 7
n[17] = 9
n[18] = 8
n[19] = 8
n[20] = 6
n[30] = 6
n[40] = 5
n[50] = 5
n[60] = 5
n[70] = 7
n[80] = 6
n[90] = 6
n[1000] = 11
nums = n.keys()


onetohundred = -1
def sum_to(start, end):
    sum_val = 0
    for i in range(start, end + 1):
        sum_val += length_of_word(i)
    return sum_val

def length_of_word(number):
    if number < 0:
        print("Incorrect usage of length_of_word using number: " + number)
        return -1
    val = 0
    # If it's in the defined dict, use it right away
    if number in nums:
        val += n[number]
    # If it's not, slice a digit and try again 
    else:
        tens = number % 100
        hundreds = number - tens
        # If hundreds =/= 0 and tens =/= 0, needs and, +3
        if hundreds != 0 and tens != 0:
            val += 3
        # Add the length of the one hundreds
        if(n[hundreds//100] != 0):
            val += n[hundreds//100] + 7
        # Add length of tens and ones
        if tens in nums:
            val += n[tens]
        else:
            ones = tens % 10
            tens -= ones
            val += n[ones] + n[tens]
    return val

def sum_one_to_hundred():
    global onetohundred
    if onetohundred > 0:
        return onetohundred
    sum_val = sum_to(1,100)
    onetohundred = sum_val
    return sum_val
print(sum_one_to_hundred())
# sum_one_to_hundred()
