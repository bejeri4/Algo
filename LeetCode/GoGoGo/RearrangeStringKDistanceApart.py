import heapq as hq
import queue

def getPQ(s):
	dct = dict()
	for ch in s:
		if ch not in dct:
			dct[ch] = 0
		dct[ch] += 1
	heap = []
	for key in dct:
		hq.heappush(heap, (-dct[key], key))
	return heap


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        result = ""
        q = queue.Queue()
        heap = getPQ(s)
        if k == 0:
            return s
        while heap:
            cnt, cur = hq.heappop(heap)
            if q.qsize() < k:
                q.put((cnt, cur))
            if q.qsize() == k:
                prevCnt, prevCh = q.get()
                prevCnt += 1
                if prevCnt < 0:
                    hq.heappush(heap, (prevCnt, prevCh))
                result += prevCh
        while not q.empty():
            cnt, ch = q.get()
            if cnt != -1:
                return ""
            else:
                result += ch
        return result
