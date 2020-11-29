# https://www.interviewbit.com/problems/city-tour/

p = 1000000007

def divideModP(a, b):
    return a * pow(b, p - 2, p)

def getC(facts, m, n):
    res = divideModP(facts[m], facts[m - n])  % p
    return divideModP(res, facts[n]) %  p


def fillFactorials(facts):
    for i in range(2, len(facts)):
        facts[i] = (facts[i - 1] * i) % p

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        facts = [1] * (A + 1)
        fillFactorials(facts)
        result = 1
        B.sort()
        gaps = []
        unvisitedCount = 0
        
        for i in range(1, len(B)):
            if B[i] != B[i - 1] + 1:
                gaps.append((B[i - 1], B[i]))
                unvisitedCount += (B[i] - B[i - 1] - 1)

        if B[0] != 1:
            unvisitedCount += B[0] - 1

        if B[-1] != A:
            unvisitedCount += A - B[-1]
            
        
        if B[0] != 1:
            result = (result * getC(facts, unvisitedCount, B[0] - 1)) % p
            unvisitedCount -= (B[0] - 1)

        if B[-1] != A:
            result = (result * getC(facts, unvisitedCount, A - B[-1])) % p
            unvisitedCount -= (A - B[-1])
        
        for gap in gaps:
                result = (result * pow(2, gap[1] - gap[0] - 2, p)) % p
                result = (result * getC(facts, unvisitedCount, gap[1] - gap[0] - 1)) % p
                unvisitedCount -= (gap[1] - gap[0] - 1)
        return result
            
            
