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
        print('y',y)
        a=y[len(y)-n].next
        print('a',a)
        b=0
        if(len(y)>1 and n>1):
            if(n!=len(y)):
                y[len(y)-n-1].next=a
                b=y[0]
            else:
                y[-2].next=a
        else:
             b=None
        
        return b