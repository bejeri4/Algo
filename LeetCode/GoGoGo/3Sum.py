def twoSum(nums, i, result):
    seen = set()
    j = i + 1
    while j < len(nums):
        c = -(nums[i] + nums[j])
        if c in seen:
            result.append([nums[i], nums[j], c])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, result)
        return result


