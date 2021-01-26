# https://www.interviewbit.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        head = None
        cur = None
        while True:
            minElem = float("inf")
            minIndex = -1
            for i in range(len(A)):
                if not A[i]:
                    continue
                if A[i].val < minElem:
                    minIndex = i
                    minElem = A[i].val
            if minIndex == -1:
                return head
            else:
                if not cur:
                    cur = A[minIndex]
                    head = cur
                else:
                    cur.next = A[minIndex]
                    cur = cur.next
                A[minIndex] = A[minIndex].next
