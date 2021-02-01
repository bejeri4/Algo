# https://www.interviewbit.com/problems/balanced-binary-tree/

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


def isBalancedRec(head):
    if not head:
        return (0, True)
    lHeight = 0
    rHeight = 0
    lBalaced = True
    rBalaced = True
    if head.left:
        lHeight, lBalaced = isBalancedRec(head.left)
        lHeight += 1
    if head.right:
        rHeight, rBalaced = isBalancedRec(head.right)
        rHeight += 1
    height = max(lHeight, rHeight)
    balanced = lBalaced and rBalaced and abs(lHeight - rHeight) < 2
    return (height, balanced)

class Solution:
	# @param A : root node of tree
	# @return an integer
    def isBalanced(self, A):
        if isBalancedRec(A)[1]:
            return 1
        else:
            return 0
