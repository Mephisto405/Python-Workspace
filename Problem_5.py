# Problem 5: Smallest multiple
"""
Q.
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#GCD
def gcd(a,b):
    q = a/b
    r = a%b
    if r == 0:
        return b
    return gcd(b,r)

#LCM
def lcm(a,b):
    return a*b/gcd(a,b)

#Smallest Multiple
def SM(n):
    if n == 2:
        return 2
    return lcm(SM(n-1),n)
