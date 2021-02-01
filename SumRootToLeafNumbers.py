# https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

p = 1003

def findSum(root, curPath, result):
    if not root:
        return
    if not root.left and not root.right:
        curPath += str(root.val)
        num = int(curPath) % p
        result[0] = (result[0] + num) % p
        return
    if root.left:
        findSum(root.left, curPath + str(root.val), result)
    if root.right:
        findSum(root.right, curPath + str(root.val), result)

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        result = [0]
        findSum(A, "", result)
        return result[0]
