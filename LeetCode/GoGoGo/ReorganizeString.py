import heapq as hq

class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - ord("a")] += 1
        heap = []
        for i in range(26):
            if arr[i] > 0:
                hq.heappush(heap, (-arr[i], chr(ord("a") + i)))
        cd = None
        while heap:
            cnt, ch = hq.heappop(heap)
            if not cd:
                cd = (cnt + 1, ch)
            else:
                result += cd[1]
                if cd[0] < 0:
                    hq.heappush(heap, (cd[0], cd[1]))
                cd = (cnt + 1, ch)
        result += cd[1]
        if len(result) < len(s):
            return ""
        return result
