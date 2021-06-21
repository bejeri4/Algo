class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        allSum = sum(stones)
        dp = [False] * (allSum + 1)
        dp[0] = True
        curS = 0
        for stone in stones:
            curS += stone
            i = curS
            while i >= stone:
                dp[i] |= dp[i - stone]
                i -= 1
        for i in range(allSum // 2, -1, -1):
            if dp[i]:
                return allSum - i - i
        return 0
