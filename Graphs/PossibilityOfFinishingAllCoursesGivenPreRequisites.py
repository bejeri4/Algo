# https://www.interviewbit.com/problems/possibility-of-finishing-all-courses-given-prerequisites/

import queue

def convertIntoGraph(A, B, C):
    nodes = []
    for _ in range(A):
        nodes.append([])
    for i in range(len(B)):
        nodes[B[i] - 1].append(C[i] - 1)
    return nodes


def containsCycleFrom(start, nodes):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        curNode = q.get()
        visited.add(curNode)
        for neig in nodes[curNode]:
            if neig in visited:
                return True
            q.put(neig)
    return False

def containsCycle(nodes):
    for i in range(len(nodes)):
        if containsCycleFrom(i, nodes):
            return True
    return False

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        nodes = convertIntoGraph(A, B, C)
        return 0 if containsCycle(nodes) else 1
