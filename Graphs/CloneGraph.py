# https://www.interviewbit.com/problems/clone-graph/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


def clone(root, cloned):
    if not root:
        return None
    if root.label in cloned:
        return root
    newNode = UndirectedGraphNode(root.label)
    cloned[newNode.label] = newNode
    for neig in root.neighbors:
        if neig.label in cloned:
            newNode.neighbors.append(cloned[neig.label])
        else:
            newNode.neighbors.append(clone(neig, cloned))
    return newNode


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        cloned = dict()
        return clone(node, cloned)
        
