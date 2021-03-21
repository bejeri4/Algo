# https://www.interviewbit.com/problems/highest-product/

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        if not A or len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        if len(A) == 2:
            return A[0] * A[1]
        A.sort()
        v1 = A[-1] * A[-2] * A[-3]
        v2 = A[0] * A[1] * A[-1]
        return max(v1, v2)
