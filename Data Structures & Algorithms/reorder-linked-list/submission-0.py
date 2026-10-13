# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0
        m=head
        while (m):
            n=n+1
            m=m.next
        p=head
        q=[]
        while(p):
            q.append(p)
            p=p.next
        r=head
        a,b=0,len(q)-1
        while(a<b):
            
            q[a].next=q[b]
            a=a+1
            if (a>=b):
                break
            q[b].next=q[a]
            b=b-1
        q[a].next=None

            

        
    

        
            
            
            


                
