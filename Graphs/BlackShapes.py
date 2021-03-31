# https://www.interviewbit.com/problems/black-shapes/

import queue

def merge(a, b):
    return 10 * a + b
    
def separate(merged):
    return merged // 10, merged % 10

def getNeigbours(a, b, matrix):
    result = []
    if a - 1 >= 0 and matrix[a - 1][b] == "X":
        result.append((a - 1, b))
    if a + 1 < len(matrix) and matrix[a + 1][b] == "X":
        result.append((a + 1, b))
    if b - 1 >= 0 and matrix[a][b - 1] == "X":
        result.append((a, b - 1))
    if b + 1 < len(matrix[a]) and matrix[a][b + 1] == "X":
        result.append((a, b + 1))
    return result
                

def bfs(a, b, matrix, visited):
    if (a, b) in visited or matrix[a][b] != "X":
        return 0
    q = queue.Queue()
    q.put((a, b))
    visited.add((a, b))
    while not q.empty():
        curI, curJ = q.get()
        neigs = getNeigbours(curI, curJ, matrix)
        for neig in neigs:
            if neig not in visited:
                q.put(neig)
                visited.add(neig)
    return 1

class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        result = 0
        visited = set()
        for i in range(len(A)):
            line = A[i]
            for j in range(len(line)):
                result += bfs(i, j, A, visited)
        return result
