# O(n ^ 2) O(n ^ 2)

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

    
    
# O(n ^ 2) O(1)
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s or s == "":
            return ""
        result = s[0]
        for c in range(2 * len(s) - 1):
            left, right = None, None
            if c % 2 == 0:
                left = c // 2 - 1
                right = c // 2 + 1
            else:
                left = c // 2
                right = c // 2 + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 > len(result):
                result = s[left: right + 1]
        return result
