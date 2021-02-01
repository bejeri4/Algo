# https://www.interviewbit.com/problems/least-common-ancestor/

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def findPath(root, elem, path):
    if not root:
        return False
    if root.val == elem:
        path.insert(0, root.val)
        return True
    if findPath(root.left, elem, path):
        path.insert(0, root.val)
        return True
    if findPath(root.right, elem, path):
        path.insert(0, root.val)
        return True
    return False

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        path1 = []
        findPath(A, B, path1)
        path2 = []
        findPath(A, C, path2)
        result = -1
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                result = path1[i]
            i += 1
        return result
