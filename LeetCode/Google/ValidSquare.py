import itertools

def dist(p1, p2):
    return pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)

def diagsAreEqual(p1, p2, p3, p4):
    return dist(p2, p4) != 0 and dist(p2, p4) == dist(p1, p3)

def isValid(p1, p2, p3, p4):
    return dist(p1, p4) != 0 and dist(p1, p4) == dist(p2, p1) and dist(p1, p4) == dist(p3, p2) and dist(p1, p4) == dist(p3, p4) and diagsAreEqual(p1, p2, p3, p4)
	

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        arr = [p1, p2, p3, p4]
        perms = itertools.permutations(arr)
        for perm in perms:
            if isValid(perm[0], perm[1], perm[2], perm[3]):
                return True
        return False
