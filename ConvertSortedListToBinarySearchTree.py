# https://www.interviewbit.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def convert(arr):
    if not arr or len(arr) == 0:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = convert(arr[:mid])
    root.right = convert(arr[mid + 1:])
    return root

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        arr = []
        while A:
            arr.append(A.val)
            A = A.next
        return convert(arr)
            
