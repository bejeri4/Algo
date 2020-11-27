# https://www.interviewbit.com/problems/single-number/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for elem in A:
            result = result ^ elem
        return result
