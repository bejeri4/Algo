from functools import cmp_to_key

def cmp(a, b):
	return a[1] - b[1]

def bSearch(arr, index):
	left = 0
	right = index - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid][1] <= arr[index][0]:
			if arr[mid + 1][1] > arr[index][0]:
				return mid
			else:
				left = mid + 1
		else:
			right = mid - 1
	return -1


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if not startTime:
            return 0
        arr = []
        for i in range(len(startTime)):
            arr.append((startTime[i], endTime[i], profit[i]))
        arr.sort(key = cmp_to_key(cmp))
        dp = []
        dp.append(arr[0][2])
        for i in range(1, len(arr)):
            p = arr[i][2]
            prev = bSearch(arr, i)
            if prev != -1:
                p += dp[prev]
            dp.append(max(dp[-1], p))
        return dp[-1]

