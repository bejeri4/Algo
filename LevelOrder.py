# https://www.interviewbit.com/problems/level-order/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def traverse(root, curD, result):
    if not root:
        return
    if len(result) <= curD:
        newLevel = []
        newLevel.append(root.val)
        result.append(newLevel)
    else:
        result[curD].append(root.val)
    traverse(root.left, curD + 1, result)
    traverse(root.right, curD + 1, result)

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        result = []
        traverse(A, 0, result)
        return result
