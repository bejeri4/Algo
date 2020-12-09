# https://www.interviewbit.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def insert(head, val):
    newNode = ListNode(val)
    if val < head.val:
        newNode.next = head
        head = newNode
        return head
    cur = head
    last = cur
    while cur != None:
        if val < cur.val:
            last.next = newNode
            newNode.next = cur
            return head
        last = cur
        cur = cur.next
    last.next = newNode
    return head

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        curEnd = A
        while curEnd != None and curEnd.next != None:
            val = curEnd.next.val
            if val < curEnd.val:
                curEnd.next = curEnd.next.next
                A = insert(A, val)
            else:
                curEnd = curEnd.next
        return A
