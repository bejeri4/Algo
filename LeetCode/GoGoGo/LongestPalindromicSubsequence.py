def fillFirstRowAndCol(dp):
	for i in range(len(dp[0])):
		dp[0][i] = 0
	for i in range(len(dp)):
		dp[i][0] = 0

def getLCS(a, b):
	dp = []
	for i in range(len(a) + 1):
		dp.append([None] * (len(b) + 1))
	fillFirstRowAndCol(dp)
	for i in range(1, len(dp)):
		for j in range(1, len(dp[i])):
			if a[i - 1] == b[j - 1]:
				dp[i][j] = 1 + dp[i - 1][j - 1]
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
	return dp[-1][-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return getLCS(s, "".join(reversed(s)))
