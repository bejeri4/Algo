# https://www.interviewbit.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getLen(head):
    result = 0
    while head != None:
        head = head.next
        result += 1
    return result
    
    
def getHalfs(head):
    secondHead = None
    size =  math.ceil(getLen(head) / 2)
    cur = head
    size -= 1
    while size > 0:
        cur = cur.next
        size -= 1
    secondHead = cur.next
    cur.next = None
    return (head, secondHead)
    
    
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
    
    
    
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        fh, sh = getHalfs(A) # first half, second half
        sh = reverse(sh)
        while sh != None:
            nodeToInsert = sh
            tmpF = fh.next
            tmpS = sh.next
            fh.next = nodeToInsert
            nodeToInsert.next = tmpF
            fh = tmpF
            sh = tmpS
            
        return A
        
