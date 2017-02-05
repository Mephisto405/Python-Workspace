# Problem_14: Longest Collatz sequence
"""
Q.
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

#Brute Force
def lenColSeq(n):
    cnt = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        cnt += 1
    return cnt

def Main(n):
    sup = 0
    for i in range(1, n):
        length = lenColSeq(i)
        if sup < length:
            sup = length
            supItem = i
    print supItem   
