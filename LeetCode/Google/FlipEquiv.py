# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(r1, r2):
    if r1 == None and r2 == None:
        return True
    if not r1 or not r2:
        return False
    if r1.val != r2.val:
        return False
    return (helper(r1.left, r2.left) and helper(r1.right, r2.right)) or (helper(r1.left, r2.right) and helper(r1.right, r2.left))

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return helper(root1, root2)
