from functools import cmp_to_key

def cmp(a, b):
	if a[0] == b[0]:
		return b[1] - a[1]
	return a[0] - b[0]


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = cmp_to_key(cmp))
        dp = []
        for i in range(len(envelopes)):
            index = bisect_left(dp, envelopes[i][1])
            if index == len(dp):
                dp.append(envelopes[i][1])
            else:
                dp[index] = envelopes[i][1]
        return len(dp)
