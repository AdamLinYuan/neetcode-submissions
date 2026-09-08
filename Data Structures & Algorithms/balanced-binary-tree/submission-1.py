# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.diff = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        if self.diff > 1:
            return False
        return True

    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diff = max(self.diff, abs(left - right))
        return 1 + max(left, right)
        