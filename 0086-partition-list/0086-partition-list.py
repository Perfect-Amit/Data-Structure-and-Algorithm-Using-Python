class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)
        s = small
        l = large
        curr = head
        while curr:
            if curr.val < x:
                s.next = curr
                s = s.next
            else:
                l.next = curr
                l = l.next
            curr = curr.next
        l.next = None
        s.next = large.next
        return small.next