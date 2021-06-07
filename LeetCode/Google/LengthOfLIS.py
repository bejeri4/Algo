# O(n ^ 2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# O(n * log(n))
class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)
        dp = []
        for i in nums:
            index = bisect_left(dp, i)
            if index == len(dp):
                dp.append(i)
            else:
                dp[index] = i
        return len(dp)

