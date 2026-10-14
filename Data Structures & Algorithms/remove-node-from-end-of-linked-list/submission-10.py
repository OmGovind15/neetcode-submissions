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
       
       
       
        
        if(len(y)-n==0):
            return head.next
        else:
            y[len(y)-n-1].next=y[len(y)-n].next
            return head
        
        