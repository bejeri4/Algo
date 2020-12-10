# https://www.interviewbit.com/problems/k-reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverseK(node, k):
    if k < 2 or not node:
        return (node, node)
    cur = node.next
    last = node
    k -= 1
    while k > 1:
        tmp = cur.next
        cur.next = last
        last = cur
        cur = tmp
        k -= 1
    otherChain = cur.next
    node.next = otherChain
    cur.next = last
    return (cur, node)
    

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B == 1 or not A or A.next == None:
            return A
        newHead = None
        lastTail = None
        while True:
            h, t = reverseK(A, B)
            if not newHead:
                newHead = h
            if not lastTail:
                lastTail = t
            else:
                lastTail.next = h
                lastTail = t
            if not t.next:
                break
            A = t.next
        return newHead
