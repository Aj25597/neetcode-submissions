# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSubtreeHelper(self,r,s):
        if not s:
            return True
        if not r:
            return False
        if self.sameTree(r,s):
            return True
        return self.isSubtreeHelper(r.left,s) or self.isSubtreeHelper(r.right,s)

    
    
    def sameTree(self,r,s):
        if not r and not s:
            return True
        if r and s and s.val == r.val:
            return (self.sameTree(r.left,s.left)) and self.sameTree(r.right,s.right)    


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtreeHelper(root,subRoot)