# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse(head):
    if not head:
        return None
    if head.next == None:
        return head
    last = head
    cur = head.next
    last.next = None
    while cur != None and cur.next != None:
        tmp = cur.next
        cur.next = last
        last = cur
        cur = tmp
    cur.next = last
    return cur
    
    
def reverseRec(head):
    if not head:
        return None
    if head.next == None:
        return head
    recReversed = reverseRec(head.next)
    head.next.next = head
    head.next = None
    return recReversed
