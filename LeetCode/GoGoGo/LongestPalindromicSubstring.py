class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or s == "":
            return ""
        dp = []
        for i in range(len(s)):
            dp.append([False] * len(s))
            dp[i][i] = True
        result = s[0]
        for length in range(2, len(s) + 1):
            for right in range(length - 1, len(s)):
                left = right - length + 1
                if length == 2:
                    if s[left] == s[right]:
                        dp[left][right] = True
                else:
                    if dp[left + 1][right - 1] and s[left] == s[right]:
                        dp[left][right] = s[left: right + 1]
                if dp[left][right] and length > len(result):
                    result = s[left: right + 1]
        return result
