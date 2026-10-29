# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthHelper(self,root,lvl):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            #Max Depth for a child
            return lvl
        else:
            return max(self.maxDepthHelper(root.left,lvl+1),self.maxDepthHelper(root.right,lvl+1))
        




    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return self.maxDepthHelper(root,1)