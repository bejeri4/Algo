# https://www.interviewbit.com/problems/maximum-absolute-difference/

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if not A:
            return 0
        plus = []
        minus = []
        for i in range(len(A)):
            plus.append(A[i] + i)
        for i in range(len(A)):
            minus.append(A[i] - i)
        plus.sort()
        minus.sort()
        r1 = abs(plus[0] - plus[-1])
        r2 = abs(minus[0] - minus[-1])
        return max(r1, r2)
