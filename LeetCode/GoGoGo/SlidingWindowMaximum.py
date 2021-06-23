def getDP(nums, k, range):
	result = [0] * len(nums)
	curMax = -math.inf
	curBucket = 0
	for i in range:
		newBucket = i // k
		if curBucket == newBucket:
			curMax = max(curMax, nums[i])
		else:
			curMax = nums[i]
			curBucket = newBucket
		result[i] = curMax
	return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = getDP(nums, k, range(len(nums)))
        right = getDP(nums, k, range(len(nums) - 1, -1, -1))
        s = 0
        result = []
        for e in range(k  - 1, len(nums)):
            if s // k == e // k:
                result.append(right[s])
            else:
                result.append(max(right[s], left[e]))
            s += 1
        return result

