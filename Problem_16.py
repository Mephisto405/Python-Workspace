# Problem_16: Power digit sum
"""
Q.
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
#Use a list for big-integer multiplication
def bigIntMult(integer,n=2):
    for i in range(len(integer)):
        integer[i] *= n
    for i in range(len(integer)):
        digit = integer[i]
        if (digit*n >= 10) & (i+1 < len(integer)):
            integer[i] = (digit)%10
            integer[i+1] += (digit)/10 #when matrix is large enough, no overflow
        else:
            continue

#main
integer = [0 for i in range(400)]
integer[0] = 1

for i in range(int(raw_input())):
    bigIntMult(integer,2)
    print integer
    print

s=0
for i in integer:
    s += i
    
print s
