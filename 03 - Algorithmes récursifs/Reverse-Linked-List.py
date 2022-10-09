class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        newhead=head
        if head.next:
            newhead= self.reverseList(head.next)
            head.next.next=head
        head.next=None
            
        return newhead