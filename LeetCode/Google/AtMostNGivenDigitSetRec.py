
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        dp = [0] * len(n) + [1]
        for i in range(len(n) - 1, -1, -1):
            for d in digits:
                if d < n[i]:
                    dp[i] += pow(len(digits), len(n) - i - 1)
                elif d == n[i]:
                    dp[i] += dp[i + 1]
        result = dp[0]
        for i in range(1, len(n)):
            result += pow(len(digits), i)
        return result
