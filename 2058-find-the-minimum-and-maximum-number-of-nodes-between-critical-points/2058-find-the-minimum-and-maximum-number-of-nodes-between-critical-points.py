class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical=[]
        pos=1
        prev=head
        curr=head.next
        while curr and curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                critical.append(pos)
            prev=curr
            curr=curr.next
            pos+=1
        if len(critical)<2:
            return [-1,-1]
        minimum=min(critical[i]-critical[i-1] for i in range(1,len(critical)))
        maximum=critical[-1]-critical[0]
        return [minimum,maximum]