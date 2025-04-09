# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        result = []

        def dfs(tree, i):
            if tree.left:
                dfs(tree.left, i+1)
            if tree.right:
                dfs(tree.right, i+1)
            if tree.left is None and tree.right is None:
                result.append(i)

        if root is None:
            result.append(0)
        else:
            dfs(root, 1)
        
        return max(result)