import heapq as hq

def initPQAndSet(heightMap, vsited):
	heap = []
	for i in range(len(heightMap)):
		for j in range(len(heightMap[i])):
			if i == 0 or i == len(heightMap) - 1 or j == 0 or j == len(heightMap[i]) - 1:
				hq.heappush(heap, (heightMap[i][j], (i, j)))
				vsited.add((i, j))
	return heap

def getNeigs(i, j, heightMap):
	result = []
	if i - 1 >= 0:
		result.append((i - 1, j))
	if i + 1 < len(heightMap):
		result.append((i + 1, j))
	if j - 1 >= 0:
		result.append((i, j - 1))
	if j + 1 < len(heightMap[0]):
		result.append((i, j + 1))

	return result


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        vsited = set()
        heap = initPQAndSet(heightMap, vsited)
        result = 0
        maxH = None
        while heap:
            height, indices = hq.heappop(heap)
            i, j = indices
            if not maxH:
                maxH = height
            elif height > maxH:
                maxH = height
            for neig in getNeigs(i, j, heightMap):
                if neig not in vsited:
                    heightOfNeig = heightMap[neig[0]][neig[1]]
                    if heightOfNeig < maxH:
                        result += (maxH - heightOfNeig)
                    hq.heappush(heap, (heightOfNeig, neig))
                    vsited.add(neig)
        return result
