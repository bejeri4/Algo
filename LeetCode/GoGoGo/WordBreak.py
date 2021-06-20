class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i: j + 1] in st and (i == 0 or dp[i - 1]):
                    dp[j] = True
            if dp[-1]:
                return True
        return False
