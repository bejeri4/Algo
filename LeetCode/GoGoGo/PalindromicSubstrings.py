class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        for _ in range(len(s)):
            dp.append([False] * len(s))
        result = 0
        for length in range(1, len(s) + 1):
            for right in range(length - 1, len(s)):
                left = right - length + 1
                if left == right:
                    dp[left][right] = True
                else:
                    if s[left] == s[right]:
                        if right - left == 1:
                            dp[left][right] = True
                        else:
                            dp[left][right] = dp[left + 1][right - 1]
                    else:
                        dp[left][right] = False
                if dp[left][right]:
                    result += 1
        return result
