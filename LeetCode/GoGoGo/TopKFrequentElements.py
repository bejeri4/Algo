import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = dict()
        for elem in nums:
            if elem not in dct:
                dct[elem] = 0
            dct[elem] += 1
        heap = []
        for key in dct:
            hq.heappush(heap, (-dct[key], key))
        result = []
        for _ in range(k):
            result.append(hq.heappop(heap)[1])
        return result
