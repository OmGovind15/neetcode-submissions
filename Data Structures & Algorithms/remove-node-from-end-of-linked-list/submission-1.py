# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=head
        y=[]
        while(x):
            y.append(x)
            x=x.next
        
        a=y[-n].next
        if(len(y)>1):
            y[len(y)-n-1].next=a
            b=y[0]
        else:
             b=None
        
        return b