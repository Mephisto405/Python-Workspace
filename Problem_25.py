# Problem_25: 1000-digit Fibonacci number
"""
Q.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
#Sub-routine for bigIntSum()
def bigIntSumSub(bigInt1, bigInt2):
    for i in range(len(bigInt2)):
        bigInt1[i] += bigInt2[i]
    for i in range(len(bigInt1)):
        q = bigInt1[i]/10
        r = bigInt1[i]%10
        bigInt1[i] = r
        if i+1 < len(bigInt1):
            bigInt1[i+1] += q
        elif q!=0:
            bigInt1.append(q)
    return bigInt1

#Use the list structure for big-integer Summation
def bigIntSum(bigInt1, bigInt2):
    if len(bigInt1) > len(bigInt2):
        return bigIntSumSub(bigInt1,bigInt2)
    else:
        return bigIntSumSub(bigInt2,bigInt1)
    
def fiboBigInt(n = 1000):
    f1 = [1]
    f2 = [1]
    index = 2
    while len(f2) < n:
        #f3,f2,f1 = bigIntSum(f3,f2),f3,f2
        tmp = f2[:] #Cautionn! Don't use tmp = f2 ( copy the reference )
        f2 = bigIntSum(f2,f1)
        f1 = tmp
        index += 1
    return index
