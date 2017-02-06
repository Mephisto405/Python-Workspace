# Problem_20: Factorial digit sum
"""
Q.
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
#Just like problem_16.py, use the list structure for big-integer multiplication
def bigIntMult(integer,n):
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
integer = [0 for i in range(200)]
integer[0] = 1

for i in range(1,101):
    bigIntMult(integer,i)

print reduce(lambda x,y : x+y, integer)
