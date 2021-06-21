class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                prev = max(dp[j], j) * max(dp[i - j], i - j)
                dp[i] = max(dp[i], prev)
        return dp[-1]
