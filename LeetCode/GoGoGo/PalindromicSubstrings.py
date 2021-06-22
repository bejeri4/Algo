# O(n ^ 2) O(n ^ 2)

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


# O(n ^ 2) O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for c in range(1, 2 * len(s)):
            left, right = None, None
            if c % 2 == 0:
                left = c // 2 - 1
                right = c // 2
            else:
                left = c // 2
                right = c // 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result
