# https://www.interviewbit.com/problems/subarrays-with-distinct-integers/

def fillPrevs(A, prevs):
    d = {}
    for i in range(len(A)):
        elem = A[i]
        if elem in d:
            prevs[i] = d[elem]
            d[elem] = i
        else:
            d[elem] = i
            
            
def fillNexts(A, nexts):
    d = {}
    for i in range(len(A) - 1, -1, -1):
        elem = A[i]
        if elem in d:
            nexts[i] = d[elem]
            d[elem] = i
        else:
            d[elem] = i


def solveAtmostB(A, B):
    if B == 0:
        return 0
    prevs = [-1] * len(A)
    nexts = [-1] * len(A)
    fillPrevs(A, prevs)
    fillNexts(A, nexts)
    i = 0
    j = 0
    numD = 0
    result = 0
    while j < len(A):
        if prevs[j] == -1 or prevs[j] < i:
            numD += 1
        if numD > B:
            k = i
            while True:
                if nexts[k] == -1 or nexts[k] > j:
                    break
                k += 1
            i = k + 1
            numD -= 1
        result += j - i + 1
        j += 1
    return result


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return solveAtmostB(A, B) - solveAtmostB(A, B - 1)
