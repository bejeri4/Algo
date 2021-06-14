from functools import cmp_to_key

def cmp(a, b):
	if a[0] == b[0]:
		return a[1] - b[1]
	return a[0] - b[0]


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort(key = cmp_to_key(cmp))
        times = []
        for p, s in arr:
            times.append((target - p) / s)
        largest = times[-1]
        result = len(times)
        print(times)
        for i in range(len(times) - 2, - 1, -1):
            if times[i] <= largest:
                result -= 1
            else:
                largest = times[i]
        return result
