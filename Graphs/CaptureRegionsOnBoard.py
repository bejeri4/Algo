import Queue

def getNeigs(i, j, A):
    result = []
    arr = [ (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j) ]
    for node in arr:
        if node[0] >= 0 and node[0] < len(A) and node[1] >= 0 and node[1] < len(A[node[0]]) and A[node[0]][node[1]] != "X":
            result.append(node)
    return result


def mark(visited, A):
    for node in visited:
        A[node[0]][node[1]] = "X"


def bfs(startI, startJ, A):
    q = Queue.Queue()
    visited = set()
    visited.add((startI, startJ))
    q.put((startI, startJ))
    while not q.empty():
        curNode = q.get()
        if curNode[0] == 0 or curNode[0] == len(A) - 1 or curNode[1] == 0 or curNode[1] == len(A[curNode[0]]) - 1:
            return
        for neig in getNeigs(curNode[0], curNode[1], A):
            if neig not in visited:
                q.put(neig)
                visited.add(neig)
    mark(visited, A)



class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] != "X":
                    bfs(i, j, A)

