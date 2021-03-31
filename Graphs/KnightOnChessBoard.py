import queue


    
def getNeigs(A, B, curI, curJ):
    result = []
    arr = [ [curI - 2, curJ - 1], [curI - 2, curJ + 1],
            [curI - 1, curJ - 2], [curI - 1, curJ + 2],
            [curI + 1, curJ - 2], [curI + 1, curJ + 2],
            [curI + 2, curJ - 1], [curI + 2, curJ + 1]
            ]
    for p in arr:
        if p[0] >= 0 and p[0] < A and p[1] >= 0 and p[1] < B:
            result.append((p[0], p[1]))
    return result

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        C -= 1
        D -= 1
        E -= 1
        F -= 1
        visited = set()
        q = queue.Queue()
        curI = C
        curJ = D
        q.put(((curI, curJ), 0))
        visited.add((curI, curJ))
        while not q.empty():
            curP, d = q.get()
            curI, curJ = curP[0], curP[1]
            if curI == E and curJ == F:
                return d
            for neig in getNeigs(A, B, curI, curJ):
                if neig not in visited:
                    q.put((neig, d + 1))
                    visited.add(neig)
        return -1
