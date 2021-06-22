mod = 1000000007

#choose n from m
def comb(m, n, memo):
	if n > m:
		return 0
	if n == 0 or n == m:
		return 1
	if memo[m][n] is not None:
		return memo[m][n]
	res = (comb(m - 1, n - 1, memo) % mod + comb(m - 1, n, memo) % mod) % mod
	memo[m][n] = res
	return res

def numOfWaysRec(nums, memo):
	if len(nums) < 3:
		return 1
	less, more = [], []
	for elem in nums[1:]:
		if elem < nums[0]:
			less.append(elem)
		else:
			more.append(elem)
	res = comb(len(nums) - 1, len(less), memo) % mod
	res = (res * numOfWaysRec(less, memo)) % mod
	res = (res * numOfWaysRec(more, memo)) % mod
	return res


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        memo = []
        for _ in range(len(nums) + 1):
            memo.append([None] * (len(nums) + 1))
        return numOfWaysRec(nums, memo) - 1
