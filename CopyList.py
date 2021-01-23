# https://www.interviewbit.com/problems/copy-list/

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        cur = head
        while cur:
            newNode = RandomListNode(cur.label)
            newNode.next = cur.next
            cur.next = newNode
            cur = cur.next.next
        cur = head
        while cur:
            tmp = cur.next.next
            if tmp:
                cur.next.next = tmp.next
            else:
                cur.next.next = None
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = tmp
            
        return head.next
