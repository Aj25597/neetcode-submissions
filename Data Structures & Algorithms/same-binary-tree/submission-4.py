# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, p,q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        leftEquivalence = self.dfs(p.left,q.left)
        rightEquivalence = self.dfs(p.right,q.right)
        return leftEquivalence and rightEquivalence and p.val == q.val

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
        