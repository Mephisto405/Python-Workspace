# Problem_7: 10001st prime
"""
Q.
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

#Brute Force
def BF(n):
    prime_arr = [2]
    num = 3
    while len(prime_arr) < n:
        cnt = 0
        for x in prime_arr:
            if num%x == 0:
                cnt = 1
        if cnt == 0:
            prime_arr.append(num)
        num += 1
    return prime_arr[-1]
