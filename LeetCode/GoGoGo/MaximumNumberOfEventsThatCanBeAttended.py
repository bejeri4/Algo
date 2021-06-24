from functools import cmp_to_key
import heapq as hq

def cmp(a, b):
    return a[0] - b[0]

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        result = 0
        heap = []
        events.sort(key = cmp_to_key(cmp))
        today = 1
        e = 0
        while today < 100001 and e < len(events):
            if not heap:
                today = events[e][0]
            while e < len(events) and events[e][0] <= today:
                hq.heappush(heap, (events[e][1], events[e]))
                e += 1
            while heap and heap[0][0] < today:
                hq.heappop(heap)
            if heap:
                result += 1
                hq.heappop(heap)
            today += 1
        while heap:
            _, event = hq.heappop(heap)
            if event[0] <= today and event[1] >= today:
                result += 1
                today += 1
        return result
    
    
    
