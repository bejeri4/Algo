class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        curVal = 0
        result = None
        while j < len(nums):
            curVal += nums[j]
            while i < j:
                if curVal - nums[i] >= k:
                    curVal -= nums[i]
                    i += 1
                else:
                    break
            if curVal >= k:
                if not result:
                    result = (i, j)
                elif result[1] - result[0] > j - i:
                    result = (i, j)
            j += 1
        print(result)
        if result:
            return result[1] - result[0] + 1
        else:
            return -1
