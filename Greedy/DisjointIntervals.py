# https://www.interviewbit.com/problems/disjoint-intervals/

from functools import cmp_to_key

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        result = 0
        A.sort(key = cmp_to_key(cmpFn))
        maxEnd = -1
        for i in range(len(A)):
            if A[i][0] > maxEnd:
                result += 1
                maxEnd = max(A[i][1], maxEnd)
        return result
        
        
def cmpFn(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return a[1] - b[1]
