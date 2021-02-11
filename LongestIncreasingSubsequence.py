# https://www.interviewbit.com/problems/longest-increasing-subsequence/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        result = 1
        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    result = max(result, dp[i])
        return result
