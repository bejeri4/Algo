def rec(nums, curSet, curIndex, parts, used):
    if parts[curSet] == 0:
        if curSet == len(parts) - 1:
            return True
        return rec(nums, curSet + 1, 0, parts, used)
    if curIndex == len(nums) or parts[curSet] < 0:
        return False
    if rec(nums, curSet, curIndex + 1, parts, used):
        return True
    if parts[curSet] - nums[curIndex] >= 0 and not used[curIndex]:
        parts[curSet] -= nums[curIndex]
        used[curIndex] = True
        if rec(nums, curSet, curIndex + 1, parts, used):
            return True
        used[curIndex] = False
        parts[curSet] += nums[curIndex]
    return False

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        s //= k
        parts = [s] * k
        used = [False] * len(nums)
        return rec(nums, 0, 0, parts, used)
