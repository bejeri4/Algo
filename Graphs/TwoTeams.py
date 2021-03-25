# https://www.interviewbit.com/problems/two-teams/

import queue

def colorize(start, curColor, nodes, colored):
    colored[start] = curColor
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        curNode = q.get()
        curColor = (colored[curNode] + 1) % 2
        for neig in nodes[curNode]:
            if colored[neig] is None:
                colored[neig] = curColor
                q.put(neig)
            elif colored[neig] != curColor:
                return False
    return True
            

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        if not B or A == 1:
            return 1
        nodes = []
        for _ in range(A):
            nodes.append([])
        for p in B:
            nodes[p[0] - 1].append(p[1] - 1)
            nodes[p[1] - 1].append(p[0] - 1)
        colored = [None] * A
        result = True
        for i in range(A):
            if colored[i] is None:
                result = result and colorize(i, 0, nodes, colored)
        return 1 if result else 0
