import heapq as hq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        visited = set()
        hq.heappush(heap, (matrix[0][0], 0, 0))
        visited.add((0, 0))
        result = None
        for _ in range(k):
            result, i, j = hq.heappop(heap)
            if i + 1 < len(matrix) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                hq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < len(matrix[0]) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                hq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return result
