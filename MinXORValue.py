# https://www.interviewbit.com/problems/min-xor-value/

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        result = math.inf
        for i in range(1, len(A)):
            xor = A[i] ^ A[i - 1]
            if xor < result:
                result = xor
        return result
