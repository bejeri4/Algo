# https://www.interviewbit.com/problems/painters-partition-problem/

p = 10000003

def canPaint(A, B, C, maxTime):
    A -= 1
    i = 0
    curPainterTime = 0
    while i < len(C):
        curTime = C[i] % p
        if curTime > maxTime: 
            return False
        if curPainterTime + curTime > maxTime:
            A -= 1
            curPainterTime = 0
        curPainterTime = curPainterTime + curTime
        i += 1
    return  A >= 0

def multModP(a, b, p):
    result = 0
    while b > 0:
        result = (result + a) % p
        b -= 1
    return result

class Solution:
    # @param A : integer numPainters
    # @param B : integer unit
    # @param C : list of integers boards
    # @return an integer
    def paint(self, A, B, C):
        result = -1
        i = 0
        j = p
        while i <= j:
            mid = i + (j - i) // 2
            if canPaint(A, B, C, mid):
                result = mid
                j = mid - 1
            else:
                i = mid + 1
        return multModP(result, B, p)
