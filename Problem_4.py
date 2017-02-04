# Problem_4: Largest palindrome product
"""
Q.
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#Is it palindrome?
def isPalin(n):
    prev = `n` #It's Backquote
    rev = prev[::-1]
    
    if(rev == prev):
        return 1
    return 0

#Brute Force
def BF(n):
    maximum = 0
    for x in range(10**(n-1),(10**n)+1):
        for y in range(10**(n-1),(10**n)+1):
            if isPalin(x*y) & (maximum < x*y) :
                maximum = x*y
    return maximum
