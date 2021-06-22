class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * 10001
        for elem in nums:
            dp[elem] += elem
        take = 0
        skip = 0
        for elem in dp:
            curTake = skip + elem
            curSkip = max(skip, take)
            take = curTake
            skip = curSkip
        return max(take, skip)
