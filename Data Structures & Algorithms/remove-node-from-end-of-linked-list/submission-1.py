class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # --- PHASE 1: REVERSE THE LIST ---
        # This makes the "Nth from End" become the "Nth from Start"
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 'prev' is now the HEAD of the reversed list
        reversed_head = prev
        
        # --- PHASE 2: DELETE THE Nth NODE ---
        
        # Case A: If we need to delete the HEAD of the reversed list (which was the tail)
        if n == 1:
            reversed_head = reversed_head.next
            
        # Case B: If we need to delete a node inside the list
        else:
            curr = reversed_head
            # We need to stop at the node BEFORE the one we delete.
            # We move (n - 2) steps.
            # Example: To delete 2nd node, we move 0 steps (stay at head).
            for _ in range(n - 2):
                curr = curr.next
            
            # Skip the Nth node
            curr.next = curr.next.next

        # --- PHASE 3: REVERSE IT BACK ---
        # We must restore the original order before returning
        prev = None
        curr = reversed_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # --- PHASE 4: RETURN THE HEAD ---
        return prev