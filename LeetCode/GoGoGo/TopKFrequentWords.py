import heapq as hq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dct = dict()
        for w in words:
            if w not in dct:
                dct[w] = 0
            dct[w] += 1
        heap = []
        for key in dct:
            hq.heappush(heap, (-dct[key], key))
        result = []
        for _ in range(k):
            result.append(hq.heappop(heap)[1])
        return result
