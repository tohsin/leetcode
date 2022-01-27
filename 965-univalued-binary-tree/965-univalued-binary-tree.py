# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        v=root.val
        def dfs(node,v):
            if not self.ans:
                return
            if node:
                if node.val!=v:
                    self.ans=False
                    return
                dfs(node.left,v)
                dfs(node.right,v)
        dfs(root,v)
        return self.ans
                    
        