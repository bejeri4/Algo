# https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/


import sys
sys.setrecursionlimit(15000000)

def getNodes(A):
    nodes = []
    rootIndex = None
    for _ in range(len(A)):
        nodes.append([])
    for i in range(len(A)):
        if A[i] == -1:
            rootIndex = i
            continue
        nodes[A[i]].append(i)
    return (nodes, rootIndex)

def maxDepthAndDif(nodes, rootIndex, curD, difs):
    if rootIndex < 0 or rootIndex >= len(nodes):
        return curD
    if len(nodes[rootIndex]) == 0:
        difs[0] = max(difs[0], curD)
        return curD
    maxH = 0
    secMaxH = 0
    for i in nodes[rootIndex]:
        d = maxDepthAndDif(nodes, i, curD, difs) + 1
        if d >= secMaxH:
            secMaxH = d
        if d >= maxH:
            secMaxH = maxH
            maxH = d
    difs[0] = max(difs[0], maxH + secMaxH)
    return maxH


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    nodes, rootIndex = getNodes(A)
        difs = []
        difs.append(0)
        maxDepthAndDif(nodes, rootIndex, 0, difs)
        return difs[0]

