import queue

def getNeigs(a):
    result = []
    strA = str(a)
    lastD = int(strA[-1])
    if lastD != 0:
        neig = strA + str(lastD - 1)
        result.append(int(neig))
    if lastD != 9:
        neig = strA + str(lastD + 1)
        result.append(int(neig))
    return result
    

def bfs(a, b):
    result = []
    if a == 0:
        result.append(0)
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)
    while not q.empty():
        cur = q.get()
        if cur >= a and cur <= b:
            result.append(cur)
        if cur < b:
            for neig in getNeigs(cur):
                q.put(neig)
    return result

    
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
       return bfs(A, B)
