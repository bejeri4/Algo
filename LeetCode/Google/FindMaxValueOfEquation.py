import heapq as hq
import math

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
    	heap = []
    	result = -math.inf
    	for xj, yj in points:
            while heap and xj - heap[0][1] > k:
                hq.heappop(heap)
            if heap:
                result = max(result, xj + yj - heap[0][0])
            hq.heappush(heap, (xj - yj, xj))
    	return result
