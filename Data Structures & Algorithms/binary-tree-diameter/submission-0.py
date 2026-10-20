# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        a=root
        b=root.left
        c=root.right
        self.count=0
        def height(x):
            if x is None:
                return 0
            p=x.left
            q=x.right

            left=height (p)
            right=height (q)
            self.count=max(self.count,left+right)
            return 1+max(left, right )
        s=height(a)

        return self.count 
         
