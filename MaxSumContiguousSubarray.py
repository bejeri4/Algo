# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        results = []
        curSum = 0
        for elem in A:
            curSum += elem
            results.append(curSum)
            if curSum < 0:
                curSum = 0
        max = -math.inf
        for elem in results:
            if elem > max:
                max = elem
        return max
