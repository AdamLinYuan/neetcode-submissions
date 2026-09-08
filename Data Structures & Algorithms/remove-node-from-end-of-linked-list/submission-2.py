# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = self.size(curr)
        indexN = size - n
        if indexN == 0:
            return head.next

        curr = head
        for i in range(size - 1):
            if (i+1) == indexN:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
            
        
    def size(self,node):
        size = 0
        while node:
            size += 1
            node = node.next

        return size