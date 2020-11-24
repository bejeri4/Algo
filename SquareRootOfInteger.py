# https://www.interviewbit.com/problems/square-root-of-integer/

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        i = 0
        j = A
        while i <= j:
            mid = i + (j - i) // 2
            product = mid * mid
            if product == A:
                return mid
            if (mid - 1) * (mid - 1) < A and product > A:
                return mid - 1
            if product < A:
                i = mid + 1
            if product > A:
                j = mid - 1
