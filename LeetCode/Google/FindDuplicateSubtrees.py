def traverse(root, dct, result):
	if root:
		s = str(root.val) + "-" + str(traverse(root.left, dct, result)) + "-" + str(traverse(root.right, dct, result))
		if s in dct:
			if dct[s] == 1:
				result.append(root)
		else:
			dct[s] = 0
		dct[s] += 1
		return s
	else:
		return "#"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        result = []
        dct = dict()
        traverse(root, dct, result)
        return result
