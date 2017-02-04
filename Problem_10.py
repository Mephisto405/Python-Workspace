# Problem_10: Summation of primes
"""
Q.
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#Brute Force Prime Finder
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
