import heapq as hq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        hq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        result = []
        visited = set()
        visited.add((0, 0))
        for _ in range(k):
            _, curI, curJ = hq.heappop(heap)
            result.append((nums1[curI], nums2[curJ]))
            nextI = curI + 1
            nextJ = curJ + 1
            if nextI != len(nums1) and (nextI, curJ) not in visited:
                hq.heappush(heap, (nums1[nextI] + nums2[curJ], nextI, curJ))
                visited.add((nextI, curJ))
            if nextJ != len(nums2) and (curI, nextJ) not in visited:
                hq.heappush(heap, (nums1[curI] + nums2[nextJ], curI, nextJ))
                visited.add((curI, nextJ))
            if not heap:
                break
        return result
