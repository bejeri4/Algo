def getNumZerosAndOnes(s):
	z = 0
	o = 0
	for elem in s:
		if elem == "0":
			z += 1
		else:
			o += 1
	return (z, o)

def rec(strs, curIndex, m, n, memo):
	if curIndex == len(strs):
		return 0
	if memo[curIndex][m][n] is not None:
		return memo[curIndex][m][n]
	v1 = rec(strs, curIndex + 1, m, n, memo)
	v2 = -1
	numZ, numO = getNumZerosAndOnes(strs[curIndex])
	if numZ <= m and numO <= n:
		v2 = rec(strs, curIndex + 1, m - numZ, n - numO, memo) + 1
	memo[curIndex][m][n] = max(v1, v2)
	return max(v1, v2)
	


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = []
        for i in range(len(strs) + 1):
            memo.append([])
            for j in range(m + 1):
                memo[i].append([None] * (n + 1))
        return rec(strs, 0, m, n, memo)
