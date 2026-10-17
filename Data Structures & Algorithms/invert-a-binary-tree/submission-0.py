# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root is None):
            return root
        
        x=root
        
        a=x.left
        b=x.right
        x.left=b
        x.right=a
        self.invertTree(a)
        self.invertTree(b)
        return root 
        
        