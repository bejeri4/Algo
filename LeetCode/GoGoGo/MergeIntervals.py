# https://leetcode.com/problems/merge-intervals/

from functools import cmp_to_key

def cmp(a, b):
	if a[0] == b[0]:
		return a[1] - b[1]
	return a[0] - b[0]

def areOverlaping(a, b):
	return a[1] >= b[0]

def merge(a, b):
	return [a[0], max(a[1], b[1])]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []
        intervals.sort(key = cmp_to_key(cmp))
        result = [intervals[0]]
        for interval in intervals[1:]:
            if areOverlaping(result[-1], interval):
                result[-1] = merge(result[-1], interval)
            else:
                result.append(interval)
        return result
