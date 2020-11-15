# https://www.interviewbit.com/problems/largest-number/

from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        A.sort(key = cmp_to_key(Solution.compare))
        result = ""
        for elem in A:
            result += str(elem)
        while len(result) > 1 and result[0] == "0":
            result = result[1:]
        return result
        
    
    def compare(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:
            return -1
        if ab < ba:
            return 1
        return 0
