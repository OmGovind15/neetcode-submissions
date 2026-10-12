# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n=head
        l=[]
        while(len(l)==len(set(l)) and n):
            l.append(n)
            n=n.next
        if(n):
            return True
        else:
            return False

