def swap(nums, i, j):
	tmp = nums[i]
	nums[i] = nums[j]
	nums[j] = tmp

def findSwapIndex(nums, left):
	result = left + 1
	for i in range(left, len(nums)):
		if nums[i] < nums[result] and nums[i] > nums[left]:
			result = i
	return result


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                swap(nums, i - 1, findSwapIndex(nums, i - 1))
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
