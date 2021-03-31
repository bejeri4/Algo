# https://www.interviewbit.com/problems/excel-column-number/

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        result = 0
        for i in range(len(A)):
            result *= 26
            result += (ord(A[i]) - ord("A") + 1)
        return result
