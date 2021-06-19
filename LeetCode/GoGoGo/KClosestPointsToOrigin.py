from functools import cmp_to_key

def getD2(i, j):
	return i * i + j * j

def calculateDistances(points):
	result = []
	for i, j in points:
		result.append((i, j,  getD2(i, j)))
	return result

def cmp(a, b):
	return a[2] - b[2]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = calculateDistances(points)
        points.sort(key = cmp_to_key(cmp))
        result = []
        for i in range(k):
            result.append([points[i][0], points[i][1]])
        return result

