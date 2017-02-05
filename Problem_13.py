# Problem_13: Large sum
"""
Q.
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
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

#main
inputList = []
for i in range(100):
    inputList.append(raw_input()[::-1])

resultBigInt = map(int,inputList[0])
for i in range(99):
    resultBigInt = bigIntSum(resultBigInt,map(int,inputList[i+1]))

print resultBigInt[::-1][:10]
