def areOverLapped(i, j):
	if i[0] > j[0]:
		tmp = i
		i = j
		j = tmp
	return not(i[1] < j[0])
	


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        indexesToRemove = []
        s = newInterval[0]
        e = newInterval[1]
        for index in range(len(intervals)):
            i = intervals[index]
            if areOverLapped(i, newInterval):
                indexesToRemove.append(index)
                s = min(s, i[0])
                e = max(e, i[1])
        newInterval = [s, e]
        delta = 0
        for i in indexesToRemove:
            del intervals[i - delta]
            delta += 1
        insertIndex = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                insertIndex = i
                break
        intervals.insert(insertIndex, newInterval)
        return intervals
