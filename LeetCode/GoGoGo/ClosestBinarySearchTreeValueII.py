import heapq as hq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = laeft
#         self.right = right

def traverse(root, heap, k):
    if not root:
        return
    hq.heappush(heap, (abs(root.val - k), root.val))
    traverse(root.left, heap, k)
    traverse(root.right, heap, k)

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        heap = []
        traverse(root, heap, target)
        result = []
        for _ in range(k):
            result.append(hq.heappop(heap)[1])
        return result
