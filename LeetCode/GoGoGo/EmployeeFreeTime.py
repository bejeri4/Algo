"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


from functools import cmp_to_key
import heapq

def getFreeTimes(intervals):
	result = []
	if len(intervals) < 2:
		return result
	for i in range(1, len(intervals)):
		freeTime = Interval(intervals[i - 1].end, intervals[i].start)
		if freeTime.start != freeTime.end:
			result.append(freeTime)
	return result

def cmp(a, b):
	return a.start - b.start

def mergeTwoIntervals(a, b):
	return Interval(min(a.start, b.start), max(a.end, b.end))

def mergeIntervals(arr):
	if not arr:
		return []
	result = []
	result.append(arr[0])
	for time in arr[1:]:
		if time.start <= result[-1].end:
			result[-1] = mergeTwoIntervals(time, result[-1])
		else:
			result.append(time)
	return result


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flatSchedule = []
        for intervals in schedule:
            for time in intervals:
                flatSchedule.append(time)
        flatSchedule.sort(key = cmp_to_key(cmp))
        mergedSchedule = mergeIntervals(flatSchedule)
        return getFreeTimes(mergedSchedule)

        
