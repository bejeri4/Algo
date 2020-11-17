# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def isOverlaping(i, j):
    return i.start <= j.end and j.start <= i.end
    
class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        result = []
        overlaps = [False] * len(intervals)
        hasOverlap = False
        for i in range(len(intervals)):
            o = isOverlaping(intervals[i], new_interval)
            hasOverlap = hasOverlap or o
            overlaps[i] = o
        if hasOverlap:
            i = 0
            while i < len(intervals):
                if not overlaps[i]:
                    result.append(intervals[i])
                else:
                    start = min(intervals[i].start, new_interval.start)
                    while i < len(overlaps) and overlaps[i]:
                        i += 1
                    i -= 1
                    end = max(intervals[i].end, new_interval.end)
                    result.append(Interval(start, end))
                i += 1
        else:
            isAdded = False
            for interval in intervals:
                if not isAdded and new_interval.start < interval.start:
                    result.append(new_interval)
                    isAdded = True
                result.append(interval)
            if not isAdded:
                result.append(new_interval)
        return result    
