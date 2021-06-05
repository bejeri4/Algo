from functools import cmp_to_key
import heapq as hq


def cmp(a, b):
	if a[0] == b[0]:
		return a[1] - b[1]
	return a[0] - b[0]


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = cmp_to_key(cmp))
        result = 0
        heap = []
        hq.heapify(heap)
        for m in intervals:
            while heap:
                oldM = hq.heappop(heap)
                if m[0] < oldM[1][1]:
                    hq.heappush(heap, oldM)
                    break
            hq.heappush(heap, (m[1], m))
            result = max(result, len(heap))
        return result

