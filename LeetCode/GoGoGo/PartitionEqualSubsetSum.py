def rec(nums, subsetSum, i, memo):
    if subsetSum == 0:
        memo[i][subsetSum] = True
        return True
    if i == len(nums) or subsetSum < 0:
        return False
    if memo[i][subsetSum] is not None:
        return memo[i][subsetSum]
    result = rec(nums, subsetSum, i + 1, memo) or rec(nums, subsetSum - nums[i], i + 1, memo)
    memo[i][subsetSum] = result
    return result

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        memo = []
        for i in range(len(nums) + 1):
            memo.append([None] * (s // 2 + 1))
        return rec(nums, s // 2, 0, memo)
