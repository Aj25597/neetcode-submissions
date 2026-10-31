# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root):
        if root is None:
            return 0
        if root and root.left is None and root.right is None:
            return 1
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)
        if abs(leftHeight-rightHeight) > 1:
            self.balanced = False
        return max(leftHeight,rightHeight) + 1
        
        
        

    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced
