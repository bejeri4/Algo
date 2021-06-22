def fillFirstRowAndCol(dp):
	for i in range(len(dp[0])):
		dp[0][i] = 0
	for i in range(len(dp)):
		dp[i][0] = 0

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for i in range(len(text1) + 1):
            dp.append([None] * (len(text2) + 1))
        fillFirstRowAndCol(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
