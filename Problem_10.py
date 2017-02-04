# Problem_10: Summation of primes
"""
Q.
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#Brute Force Prime Finder n<200000
def BF(n):
    prime_arr = [2]
    num = 3
    while True:
        cnt = 0
        for x in prime_arr:
            if num%x == 0:
                cnt = 1
        if cnt == 0:
            if num < n:
                prime_arr.append(num)
            else:
                return reduce(lambda x,y : x + y, prime_arr)
        num += 1
    print prime_arr
    return reduce(lambda x,y : x + y, prime_arr)

#Brute Force second ver.
import math

def BF2(n):
    result = 0;
    i = 2
    while i < n:
        if isPrime(i) == 1:
            result += i
        i += 1
    return result

def isPrime(i):
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            return 0
    return 1
