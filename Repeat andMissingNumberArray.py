# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

p = 1000000007

def getExpectedSum(n):
    result = 0
    for elem in range(1, n + 1):
        result += elem
        result = result % p
    return result

def getActualSum(A):
    result = 0
    for elem in A:
        result += elem
        result = result % p
    return result
        
def getExpectedProduct(n):
    result = 1
    for elem in range(1, n + 1):
        result *= elem
        result = result % p
    return result

def getActualProduct(A):
    result = 1
    for elem in A:
        result *= elem
        result = result % p
    return result
    
def divideModP(a, b):
    return ((a % p) * pow(b, p - 2, p)) % p
    
def minusP(a, b):
    result = a - b
    if result < 0:
        result += p
    return result
        
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        expectedS = getExpectedSum(len(A))
        actualS = getActualSum(A)
        expectedP = getExpectedProduct(len(A))
        actualP = getActualProduct(A)
        
        # actualS + a - b = expectedS
        # actualP * a / b = expectedP
        b = (minusP(expectedS, actualS) * actualP) % p
        b = divideModP(b, minusP(expectedP, actualP))
        a = (minusP(expectedS, actualS) + b) % p
        return (b, a)
        
        
