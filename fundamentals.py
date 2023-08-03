# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
for num in range(-300, 1):
    if num % 3 == 0 and num not in [-3, -6]:
        print(num)

# Print integers from 2000 to 5280, using a WHILE.
num = 2000
while num <= 5280:
    print(num)
    num += 1

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


# Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
def flexible_countdown(lowNum, highNum, mult):
    for num in range(highNum, lowNum - 1, -1):
        if num % mult == 0:
            print(num)


lowNum = 2
highNum = 9
mult = 3
flexible_countdown(lowNum, highNum, mult)
