# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root) -> tuple[int, bool]:
        if root is None:
            return (0,True)
        if root and root.left is None and root.right is None:
            return (1,True)
        balanced = True
        leftHeight,leftBalanced = self.dfs(root.left)
        rightHeight,rightBalanced = self.dfs(root.right)

        balanced = abs(leftHeight - rightHeight) <= 1
        return (1 +max(leftHeight,rightHeight),leftBalanced and rightBalanced and balanced  )
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _,balanced = self.dfs(root)
        return balanced
        
        
