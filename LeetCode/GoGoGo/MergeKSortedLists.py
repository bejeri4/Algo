import heapq as hq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for head in lists:
            while head:
                hq.heappush(heap, head.val)
                head = head.next
        head = None
        tmp = None
        while heap:
            newNode = ListNode(hq.heappop(heap))
            if not head:
                head = newNode
                tmp = newNode
            else:
                tmp.next = newNode
                tmp = newNode
        return head
